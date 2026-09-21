from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
import base64

PROJECT_ENDPOINT = "https://foundry-dev-as-pac-04.services.ai.azure.com/api/projects/ai-rg-foundry-04"

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

openai = project.get_openai_client()

with open("agent_conversations.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

response = openai.responses.create(
    model="gpt-4.1-mini",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text",
             "text": "Generate a summary based on the content in the attached image"},
            {"type": "input_image",
             "image_url": f"data:image/png;base64,{b64}"},
        ],
    }],
)

print(response.output_text)