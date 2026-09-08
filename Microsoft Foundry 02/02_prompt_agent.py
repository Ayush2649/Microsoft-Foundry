from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition

PROJECT_ENDPOINT = "https://foundry-dev-as-pac-04.services.ai.azure.com/api/projects/ai-rg-foundry-04"
AGENT_NAME = "IT-HelpDesk-Support"
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
            "You are a helpful IT support assistant for a company. "
            "When a user asks a question, use the available tools to find the answer. "
            "Always use a tool before responding — do not answer from memory alone. "
            "Keep your responses clear and concise."
        ),
    ) 
)

print(f"Agent Created: ")
print(f"  ID    : {agent.id}")
print(f"  Name  : {agent.name}")
print(f"  Version : {agent.version}")