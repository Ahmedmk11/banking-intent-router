import uvicorn
from dotenv import load_dotenv
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route


from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentInterface,
    AgentSkill,
)
from a2a.server.routes import (
    create_agent_card_routes,
    create_jsonrpc_routes,
)

from executor import OrchestratorExecutor
from contextlib import asynccontextmanager
import asyncio

load_dotenv()

if __name__ == '__main__':
    
    skill = AgentSkill(
        id='orchestrator',
        name='Orchestrator Agent',
        description='Receives user banking queries, filters out non-banking requests, detects intent, and routes to the appropriate specialist agent.',
        tags=['banking', 'routing', 'guardrail', 'intent-detection'],
        examples=[
            'When will my card arrive?',
            'My transfer failed',
            'I need to verify my identity',
        ],
    )

    public_agent_card = AgentCard(
        name='Orchestrator Agent',
        description='Orchestrates user requests and routes them to the appropriate specialist agents and responds.',
        version='0.1.0',
        default_input_modes=['text/plain'],
        default_output_modes=['text/plain'],
        capabilities=AgentCapabilities(streaming=False, extended_agent_card=False),
        supported_interfaces=[
            AgentInterface(
                protocol_binding='JSONRPC',
                url='http://127.0.0.1:8000',
            )
        ],
        skills=[skill],
    )

    executor = OrchestratorExecutor()

    async def cli_loop():
        await asyncio.sleep(1)
        print("\n=== Banking Intent Router ===")
        print("Type your query (or 'quit' to exit):\n")
        
        while True:
            user_input = (await asyncio.to_thread(input, "> ")).strip()
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            if not user_input:
                continue
            
            result = await executor.agent.invoke(user_input)
            print(f"\n{result}\n")

    @asynccontextmanager
    async def lifespan(app):
        await executor.agent.initialize()
        asyncio.create_task(cli_loop())
        yield

    request_handler = DefaultRequestHandler(
        agent_executor=executor,
        task_store=InMemoryTaskStore(),
        agent_card=public_agent_card,
    )

    async def debug_route(request: Request):
        body = await request.json()
        return JSONResponse({"received_method": body.get("method")})


    routes = []
    routes.extend(create_agent_card_routes(public_agent_card))
    routes.extend(create_jsonrpc_routes(request_handler, '/'))
    routes.append(Route("/debug", debug_route, methods=["POST"]))

    app = Starlette(routes=routes, lifespan=lifespan)

    uvicorn.run(app, host='127.0.0.1', port=8000)
