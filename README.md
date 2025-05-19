# 🤖 Strands Agents Demo

A demo project showcasing the use of Strands Agents with Azure OpenAI integration.

## 🚀 Features

- 🤖 Integration with Azure OpenAI through LiteLLM
- 🛠️ Built-in tools support (calculator, current time, Python REPL)
- 🔄 Streaming responses
- 🔒 Secure credential management

## 🛠️ Setup

1. **Initialize the project with uv:**
```bash
uv init
```

2. **Install dependencies:**
```bash
uv pip install strands-agents strands-agents-tools openai litellm
```

3. **Configure environment:**
Create a `.env` file with your Azure OpenAI credentials:
```env
AZURE_API_KEY=your_api_key
AZURE_API_BASE=your_api_base
AZURE_DEPLOYMENT_NAME=your_deployment_name
AZURE_API_VERSION=2025-04-01-preview
```

## 🎮 Usage

Run the example agent:
```bash
python simple_agent.py
```

## 📁 Project Structure

```
.
├── simple_agent.py     # Main example showing how to use Strands Agents
├── litellm_provider.py # LiteLLM provider implementation
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## 🔧 Configuration

The agent can be configured with the following parameters:
- `model_id`: Azure OpenAI model to use
- `temperature`: Response creativity (0.0 to 1.0)
- `max_tokens`: Maximum response length
- `api_base`: Azure OpenAI endpoint
- `api_key`: Azure OpenAI API key
- `deployment_name`: Azure OpenAI deployment name
- `api_version`: Azure OpenAI API version

## 📝 License

MIT License
