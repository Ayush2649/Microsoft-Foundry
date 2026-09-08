from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, WebSearchTool

PROJECT_ENDPOINT = "https://foundry-dev-as-pac-04.services.ai.azure.com/api/projects/ai-rg-foundry-04"
AGENT_NAME = "web-search-lab-agent"
DEPLOYMENT_NAME = "gpt-4.1-mini-2"

client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

agent = client.agents.create_version(
    agent_name = AGENT_NAME,
    definition = PromptAgentDefinition(
        model = DEPLOYMENT_NAME,
        instructions = (
            "You are a helpful assistant. Use web search to answer questions that require current information. "
        ),
        tools = [WebSearchTool()]
    ) 
)

print(f"Agent Created: ")
print(f"  ID    : {agent.id}")
print(f"  Name  : {agent.name}")
print(f"  Version : {agent.version}")