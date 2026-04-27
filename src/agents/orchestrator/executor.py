from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.types import (
    TaskState,
    TaskStatus,
    TaskStatusUpdateEvent,
    TaskArtifactUpdateEvent,
)
from a2a.types import Task, Message, Artifact
from a2a.types import SendMessageRequest

import httpx
from a2a.client.card_resolver import A2ACardResolver

from a2a.client.client_factory import ClientFactory
from a2a.client.client import ClientConfig

from uuid import uuid4
from google.protobuf.json_format import ParseDict

SPECIALIST_URLS = [
    "http://127.0.0.1:8001",
]

class OrchestratorAgent:
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        from peft import PeftModel

        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cuda")
        transformer = self.model[0].auto_model
        peft = PeftModel.from_pretrained(transformer, "../../training/model")
        merged = peft.merge_and_unload()
        self.model[0].auto_model = merged

        import numpy as np
        import os

        self.intent_names = [f.replace("_centroid.npy", "") for f in os.listdir("../../training/centroids/finetuned")]
        self.centroids = {}

        for intent in self.intent_names:
            self.centroids[intent] = np.load(f"../../training/centroids/finetuned/{intent}_centroid.npy")

        self.agent_registry = {}
    
    async def initialize(self):
        async with httpx.AsyncClient() as httpx_client:
            for url in SPECIALIST_URLS:
                resolver = A2ACardResolver(httpx_client=httpx_client, base_url=url)
                card = await resolver.get_agent_card()
                for skill in card.skills:
                    for tag in skill.tags:
                        self.agent_registry[tag] = {"url": url, "card": card}
        
        for entry in self.agent_registry.values():
            if "client" not in entry:
                config = ClientConfig(httpx_client=httpx.AsyncClient(timeout=httpx.Timeout(60.0)))
                factory = ClientFactory(config)
                entry["client"] = factory.create(entry["card"])

    def find_intent(self, user_message):
        enc_message = self.model.encode(user_message, normalize_embeddings=True)

        similarities = {}

        for intent in self.intent_names:
            curr_centroid = self.centroids[intent]
            curr_similarity = curr_centroid @ enc_message
            similarities[intent] = curr_similarity

        best_intent = max(similarities, key=lambda x: similarities[x])
        best_score = similarities[best_intent]

        prediction = best_intent if best_score >= 0.75 else "out_of_scope"

        return prediction

    async def invoke(self, user_message: str) -> str:
        prediction = self.find_intent(user_message)

        if prediction == "out_of_scope":
            return "I'm sorry, I can only help with banking-related questions."
        
        entry = self.agent_registry.get(prediction)
        if not entry:
            return f"LOG: Intent specialist doesn't exist: {prediction}"

        client = entry["client"]
        request = ParseDict(
            {
                "message": {
                    "messageId": uuid4().hex,
                    "role": "ROLE_USER",
                    "parts": [{"text": user_message}],
                }
            },
            SendMessageRequest()
        )
        response = client.send_message(request)

        async for stream_response in response:
            if stream_response.HasField("task") and stream_response.task.artifacts:
                return stream_response.task.artifacts[0].parts[0].text
            elif stream_response.HasField("message"):
                return stream_response.message.parts[0].text
        return "No response"

class OrchestratorExecutor(AgentExecutor):
    def __init__(self):
        self.agent = OrchestratorAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        task = context.current_task or Task(
            id=context.task_id,
            context_id=context.context_id,
            history=[context.message],
        )
        await event_queue.enqueue_event(task)

        await event_queue.enqueue_event(
            TaskStatusUpdateEvent(
                task_id=context.task_id,
                context_id=context.context_id,
                status=TaskStatus(
                    state=TaskState.TASK_STATE_WORKING,
                    message=Message(
                        role="ROLE_AGENT",
                        parts=[{"text": "Processing your request..."}],
                    ),
                ),
            )
        )

        user_message = context.message.parts[0].text
        result = await self.agent.invoke(user_message)

        await event_queue.enqueue_event(
            TaskArtifactUpdateEvent(
                task_id=context.task_id,
                context_id=context.context_id,
                artifact=Artifact(
                    name="response",
                    parts=[{"text": result}]
                ),
            )
        )

        await event_queue.enqueue_event(
            TaskStatusUpdateEvent(
                task_id=context.task_id,
                context_id=context.context_id,
                status=TaskStatus(state=TaskState.TASK_STATE_COMPLETED),
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        await event_queue.enqueue_event(
            TaskStatusUpdateEvent(
                task_id=context.task_id,
                context_id=context.context_id,
                status=TaskStatus(state=TaskState.TASK_STATE_CANCELED),
            )
        )