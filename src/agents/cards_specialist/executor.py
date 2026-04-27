from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.types import (
    TaskState,
    TaskStatus,
    TaskStatusUpdateEvent,
    TaskArtifactUpdateEvent,
)
from a2a.types import Task, Message, Artifact

import anthropic
import os

class CardsAgent:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.system_prompt = """
        You are a banking cards specialist assistant.
        You help users with card-related queries such as card delivery, card activation, 
        card limits, lost or stolen cards, and card transactions.
        This is a mock environment, provide realistic but fictional responses.

        Response guidelines:
        Keep responses concise and professional. 
        Use plain text only, no markdown, no headers, no bullet points.
        Maximum 3-4 sentences. 
        Get straight to the point.
        """

    async def invoke(self, user_message: str) -> str:
        response = self.client.messages.create(
            model=os.getenv('ANTHROPIC_MODEL'),
            max_tokens=1024,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text

class CardsExecutor(AgentExecutor):
    def __init__(self):
        self.agent = CardsAgent()

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
                        parts=[{"text": "Processing your request..."}]
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
                )
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
