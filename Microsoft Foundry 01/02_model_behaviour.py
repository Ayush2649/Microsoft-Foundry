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
    # instructions= """You are a senior Azure Cloud Architect Assistant. 
    # You only answer questions related to Azure cloud services and architecture. 
    # Always structure your responses with clear headings. 
    # Use concise, technical language suitable for an experienced dveloper audience. 
    # If a question is outside the azure domain, politely decline to answer.""",
    # input="What are the three best practices for securing an Azure Storage Account?",
    # max_output_tokens=50,
    instructions="You are a creative Copywriter.",
    input="Write a two-sentence tag line for a new AI-powered productivity app that helps users manage their tasks efficiently.",
    temperature=2,
)

print(f"answer: {response.output_text}")
