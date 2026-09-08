# Microsoft Foundry Examples

Python examples for Azure AI Foundry, the OpenAI Responses API, Foundry agents, Azure AI Search, retrieval-augmented generation (RAG), and Azure Functions.

## Repository Layout

### `Microsoft Foundry 01`

Introductory Responses API examples:

- `01_first_api_call.py` - Make a basic model request.
- `02_model_behaviour.py` - Control instructions, temperature, and output length.
- `03_reasoning.py` - Ask the model to analyze an architecture problem.
- `04_multi_modal.py` - Send an image and extract its text.
- `05_we_search.py` - Use the web search tool.
- `06_code_interpretor.py` - Use the code interpreter tool.

### `Microsoft Foundry 02`

Agent and enterprise integration examples:

- `01_openai_agent.py` - Build a local agent with Python function tools.
- `02_prompt_agent.py` - Create a prompt agent in Azure AI Foundry.
- `03_invoke_agent.py` - Invoke a deployed Foundry agent.
- `04_agent_web_search.py` - Create an agent with web search.
- `05_IT_HelpDesk_Agent.py` - Create an agent with function tool definitions.
- `07_helpdesk_client.py` - Run local function tools in response to agent calls.
- `08_ai_search.py` - Query an Azure AI Search index.
- `09_customer_rag_agent.py` - Create a customer support RAG agent.
- `10_customer_rag_client.py` - Retrieve Azure AI Search results and ground an agent response.
- `06_RAG/` - Knowledge-base documents used by the customer support example.
- `CLOUDXEUS_FUNC/` - A small Azure Functions HTTP API for order data.

## Prerequisites

- Python 3.10 or later
- An Azure subscription with access to the configured Azure AI Foundry project
- An Azure AI Foundry model deployment named `gpt-4.1-mini-2`, or equivalent code changes
- Azure CLI, logged in with an identity that can access Foundry and Azure AI Search resources
- Azure Functions Core Tools for the `CLOUDXEUS_FUNC` example

Log in for examples that use Azure Identity:

```powershell
az login
```

## Setup

Create and activate a virtual environment from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the packages used by the examples:

```powershell
python -m pip install openai openai-agents azure-ai-projects azure-identity azure-search-documents azure-functions
```

The examples in `Microsoft Foundry 01` use an API key through `AZURE_OPENAI_API_KEY`. Set it in the current PowerShell session:

```powershell
$env:AZURE_OPENAI_API_KEY = "your-rotated-key"
```

Alternatively, copy `.env.example` to `.env` and load it with your preferred environment-variable tool. The scripts do not load `.env` automatically.

Do not commit `.env`, API keys, connection strings, or local Azure Function settings. The key previously present in the examples should be revoked and regenerated before sharing the repository.

## Running Examples

Run commands from the repository root. For example:

```powershell
python ".\Microsoft Foundry 01\01_first_api_call.py"
python ".\Microsoft Foundry 01\05_we_search.py"
python ".\Microsoft Foundry 02\03_invoke_agent.py"
python ".\Microsoft Foundry 02\10_customer_rag_client.py"
```

The image example expects `Agent_types.png` in the `Microsoft Foundry 01` directory. The agent examples require the Foundry project endpoint, agent names, model deployment, and permissions configured in the source files or your Azure environment.

## Azure AI Search and RAG

The customer RAG client expects:

- An Azure AI Search service and index containing `chunk`, `title`, `parent_id`, and `text_vector` fields.
- A vectorization configuration supported by the index.
- The documents from `Microsoft Foundry 02/06_RAG/` uploaded and indexed.
- An accessible Foundry project and deployed agent.

Update the endpoint, index, and agent identifiers in `10_customer_rag_client.py` when using a different Azure environment.

## Azure Functions Example

The function app exposes:

- `GET /api/orders` - List sample orders.
- `GET /api/orders/{order_id}` - Get one sample order.

Start it locally:

```powershell
cd ".\Microsoft Foundry 02\CLOUDXEUS_FUNC"
func start
```

The local settings file is intentionally ignored by Git. It currently uses the local Azure Storage emulator setting and contains no application secret.

## Security

Before pushing changes:

1. Search for accidental secrets and remove them from tracked files.
2. Store credentials in environment variables, Azure Key Vault, or managed identity.
3. Rotate any credential that has ever been committed, even if it was later removed.
4. Review the Git history if a secret was pushed and remove it using an approved history-rewrite process.
