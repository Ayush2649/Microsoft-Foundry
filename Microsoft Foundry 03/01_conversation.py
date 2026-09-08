from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT="https://foundry-dev-as-pac-04.services.ai.azure.com/api/projects/ai-rg-foundry-04"
AGENT_NAME="cloudxeus-support-agent-conv"

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

openai=client.get_openai_client()
sara=openai.conversations.create()
print(sara.id)

response=openai.responses.create(
    conversation=sara.id,
    extra_body={"agent_reference":{"name":AGENT_NAME,"type":"agent_reference"}},
    input="My order #4521 is late!!"
)

print(response.output_text)

response=openai.responses.create(
    conversation=sara.id,
    extra_body={"agent_reference":{"name":AGENT_NAME,"type":"agent_reference"}},
    input="Any update on it?"
)

print(response.output_text)