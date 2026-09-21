from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import base64

PROJECT_ENDPOINT = "https://a75923630-2998-resource.services.ai.azure.com/api/projects/a75923630-2998"
AGENT_NAME = "cloudxeus-support"

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

openai = project.get_openai_client()

with open("support.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

response = openai.responses.create(
    extra_body={"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}},
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "I'm getting this error connecting to the VPN. What does it mean?"},
                {"type": "input_image", "image_url": f"data:image/png;base64,{image_b64}"},
            ],
        }
    ],
)

print(response.output_text)
print(response.model_extra["content_filters"])