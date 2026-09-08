from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT = "https://foundry-dev-as-pac-04.services.ai.azure.com/api/projects/ai-rg-foundry-04"
AGENT_NAME = "IT-HelpDesk-Support"

client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

openai = client.get_openai_client()

response = openai.responses.create(
    extra_body={"agent_reference":{"name": AGENT_NAME, "type": "agent_reference"}},
    input="How do I reset my password?",
)

print(f"Response: {response.output_text}")