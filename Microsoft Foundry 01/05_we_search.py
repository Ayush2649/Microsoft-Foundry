import os

from openai import OpenAI

endpoint = "https://foundry-dev-as-pac-04.services.ai.azure.com/openai/v1"
deployment_name = "gpt-4.1-mini-2"
api_key = os.environ["AZURE_OPENAI_API_KEY"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful research assistant. Always cite your sources.",
    input="What are the latest developments in AI regulation in the European Union?",
    tools=[{"type": "web_search"}],
    tool_choice="auto"
)

print(f"answer: {response.output_text}")
