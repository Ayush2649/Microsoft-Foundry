import os

from langchain_openai import ChatOpenAI

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
api_key = os.environ["AZURE_OPENAI_API_KEY"]

client=ChatOpenAI(
    base_url=endpoint,
    model=deployment_name,
    api_key=api_key,
)

response=client.invoke("What are the three main benefits of using managed AI endpoints using the cloud?")
print(response.content)