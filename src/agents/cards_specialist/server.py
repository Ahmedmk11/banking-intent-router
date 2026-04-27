import uvicorn
from dotenv import load_dotenv
from starlette.applications import Starlette

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

from executor import CardsExecutor

load_dotenv()

if __name__ == '__main__':

    skill = AgentSkill(
        id='cards',
        name='Cards Specialist Agent',
        description='Handles all banking card-related queries including delivery, activation, limits, lost or stolen cards, and transactions.',
        tags=[
            'activate_my_card',
            'card_about_to_expire',
            'card_acceptance',
            'card_arrival',
            'card_delivery_estimate',
            'card_linking',
            'card_not_working',
            'card_payment_fee_charged',
            'card_payment_not_recognised',
            'card_payment_wrong_exchange_rate',
            'card_swallowed',
            'change_pin',
            'compromised_card',
            'contactless_not_working',
            'declined_card_payment',
            'disposable_card_limits',
            'get_disposable_virtual_card',
            'get_physical_card',
            'getting_spare_card',
            'getting_virtual_card',
            'lost_or_stolen_card',
            'order_physical_card',
            'passcode_forgotten',
            'pending_card_payment',
            'pin_blocked',
            'reverted_card_payment',
            'supported_cards_and_currencies',
            'virtual_card_not_working',
            'visa_or_mastercard',
        ],
        examples=[
            'When will my card arrive?',
            'My card was stolen',
            'How do I activate my card?',
        ],
    )

    public_agent_card = AgentCard(
        name='Cards Specialist Agent',
        description='Specialist agent for handling banking card-related queries.',
        version='0.1.0',
        default_input_modes=['text/plain'],
        default_output_modes=['text/plain'],
        capabilities=AgentCapabilities(streaming=False, extended_agent_card=False),
        supported_interfaces=[
            AgentInterface(
                protocol_binding='JSONRPC',
                url='http://127.0.0.1:8001',
            )
        ],
        skills=[skill],
    )

    request_handler = DefaultRequestHandler(
        agent_executor=CardsExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=public_agent_card,
    )

    routes = []
    routes.extend(create_agent_card_routes(public_agent_card))
    routes.extend(create_jsonrpc_routes(request_handler, '/'))

    app = Starlette(routes=routes)

    uvicorn.run(app, host='127.0.0.1', port=8001)
