import os

from openai import OpenAI

endpoint = "https://foundry-dev-as-pac-04.services.ai.azure.com/openai/v1"
deployment_name = "gpt-4.1-mini-2"
api_key = os.environ["AZURE_OPENAI_API_KEY"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

problem = """
A distributed e-commerce system is experiencing intermittent checkout failures 
during peak traffic. The failures appear random, affect roughly 3 percent of the transactions, 
and only occur when inventory checks and payment processing run concurrently. 
Identify the most likely root cause and propose a solution.
"""

response = client.responses.create(
    model=deployment_name,
    instructions="You are a senior software architect.",
    input=problem,
)


print(f"answer: {response.output_text}")
