"""Simple example of using Strands Agents with Azure OpenAI."""

import logging
import os
from dotenv import load_dotenv
from strands import Agent, tool
import litellm_provider
from strands_tools import calculator, current_time, python_repl

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_environment() -> None:
    """Load environment variables from .env file."""
    logger.info("Loading environment variables...")
    try:
        load_dotenv()
    except Exception as e:
        logger.error(f"Failed to load environment variables: {e}")
        raise


def create_litellm_provider() -> litellm_provider.LiteLLMModel:
    """Create and configure the LiteLLM provider.
    
    Returns:
        LiteLLMModel: Configured LiteLLM provider instance.
    """
    logger.info("Creating LiteLLM provider...")
    try:
        return litellm_provider.LiteLLMModel(
            model_id=os.getenv("AZURE_DEPLOYMENT_NAME", "azure/gpt-4o-mini"),
            temperature=0.7,
            max_tokens=1000,
            api_base=os.getenv("AZURE_API_BASE"),
            api_key=os.getenv("AZURE_API_KEY"),
            deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
            api_type="azure",
            api_version=os.getenv("AZURE_API_VERSION", "2025-04-01-preview")
        )
    except Exception as e:
        logger.error(f"Failed to create LiteLLM provider: {e}")
        raise


def create_agent(model: litellm_provider.LiteLLMModel) -> Agent:
    """Create a Strands agent with the provided model.
    
    Args:
        model: The model provider to use with the agent.
        
    Returns:
        Agent: Configured Strands agent instance.
    """
    logger.info("Creating Strands agent...")
    try:
        return Agent(model=model)
    except Exception as e:
        logger.error(f"Failed to create agent: {e}")
        raise


def run_conversation(agent: Agent, query: str) -> None:
    """Run a conversation with the agent.
    
    Args:
        agent: The Strands agent to use.
        query: The query to send to the agent.
    """
    logger.info("Starting conversation...")
    try:
        response = agent(query)
        logger.info(f"Response received: {response}")
        print(response)
    except Exception as e:
        logger.error(f"Failed to get response: {e}")
        raise


def main() -> None:
    """Run the example agent."""
    # Setup
    setup_environment()
    
    # Create provider and agent
    provider = create_litellm_provider()
    agent = create_agent(provider)
    
    # Run example conversation
    run_conversation(agent, "What is the capital of France?")


if __name__ == "__main__":
    main()
