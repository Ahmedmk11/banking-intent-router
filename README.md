# Banking Intent Router

This project is a banking intent router built with the `a2a` (Agent-to-Agent) framework. It uses a fine-tuned sentence transformer model to classify user queries and route them to the appropriate specialist agent. Fine-tuning improved the model's accuracy from 84.94% to 91.30%, resulting in a 6.36% improvement in intent classification.

## Technical Overview

The system consists of two main types of agents:

1.  **Orchestrator Agent**:
    - Acts as the primary entry point for all user queries.
    - Uses a `sentence-transformers/all-MiniLM-L6-v2` model fine-tuned with PEFT for intent classification.
    - Performs intent detection by encoding the user's message and calculating the cosine similarity against pre-computed centroids for each intent.
    - If the similarity score is above a threshold (0.75), it routes the request to the corresponding specialist agent. Otherwise, it's handled as out-of-scope.
    - The server is built using `Starlette` and `uvicorn`.

2.  **Cards Specialist Agent**:
    - A specialized agent responsible for handling all card-related banking queries.
    - Uses the Anthropic API to generate conversational responses.
    - Defines its capabilities and the intents it can handle (e.g., `card_arrival`, `lost_or_stolen_card`) in its `AgentCard`.

## Core Technologies

- **Machine Learning**:
  - `sentence-transformers`: For generating text embeddings.
  - `peft`: For efficient fine-tuning of the transformer model using Low-Rank Adaptation (LoRA).
  - `numpy`: For centroid calculations.
- **Frameworks & Libraries**:
  - `a2a`: For the underlying agent communication and server structure.
  - `Starlette` & `uvicorn`: For the asynchronous web server implementation.
  - `anthropic`: For integration with the Anthropic language model.

## Project Structure

- **`src/agents/`**: Contains the implementation for the `Orchestrator` and `Cards Specialist` agents.
- **`src/data/`**: Holds the data and notebooks (`preprocessing.ipynb`) used for training.
- **`src/training/`**: Contains notebooks for model fine-tuning (`finetune.ipynb`), centroid computation (`compute_centroids.ipynb`), and evaluation (`evaluate_embeddings.ipynb`). The fine-tuned model, centroids, and checkpoints are also stored here.
