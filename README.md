# Banking Intent Router

This project implements a banking intent router that uses a fine-tuned sentence transformer model to classify user queries and route them to specialized agents. The primary agent, the **Orchestrator**, acts as the main entry point, determining the user's intent and forwarding the request to the appropriate specialist. If the query falls outside the supported intents, the Orchestrator will inform the user that it cannot assist.

The project includes a **Cards Specialist** agent, which is equipped to handle a wide range of card-related inquiries. This specialist agent leverages a powerful language model to provide accurate and contextually relevant responses to user questions about card delivery, activation, limits, and other related topics.

## Key Features

- **Intent-Based Routing**: The Orchestrator agent uses a fine-tuned sentence transformer model to accurately identify the user's intent.
- **Specialized Agents**: The system is designed to be extensible with multiple specialist agents, each an expert in a specific domain.
- **Out-of-Scope Handling**: Queries that do not match any of the predefined intents are gracefully handled by the Orchestrator.
- **Scalable Architecture**: The project is structured to support the addition of new specialist agents as the range of supported banking services grows.

## How It Works

The core of the intent detection mechanism lies in the `OrchestratorAgent`, which performs the following steps:

1. **Encodes the user's message** into a high-dimensional vector using the fine-tuned sentence transformer model.
2. **Calculates the cosine similarity** between the user's message embedding and pre-computed centroids for each supported intent.
3. **Identifies the intent** with the highest similarity score.
4. **Routes the request** to the specialist agent registered for that intent.

If the highest similarity score is below a certain threshold (e.g., 0.75), the query is considered "out of scope."

## Project Structure

The project is organized into the following key directories:

- **`src/agents/`**: This directory contains the core logic for the Orchestrator and specialist agents.
  - **`orchestrator/`**: The main agent that routes user queries.
  - **`cards_specialist/`**: A specialized agent for handling card-related questions.
- **`src/data/`**: Includes notebooks and data for training the intent detection model.
- **`src/training/`**: Contains notebooks and artifacts related to model fine-tuning, centroid computation, and embedding evaluation.

This modular structure allows for the independent development and deployment of specialist agents, making the system flexible and easy to maintain.

## Getting Started

To run the project, you will need to install the necessary dependencies and set up the environment. The `pyproject.toml` file lists all the required packages. Once the environment is configured, you can start the Orchestrator and specialist agent servers.

The Orchestrator agent provides a command-line interface for interacting with the system. You can type your banking-related queries, and the agent will route them to the appropriate specialist for a response.

This project serves as a robust foundation for building a comprehensive, AI-powered banking assistant that can efficiently handle a wide variety of user requests.
