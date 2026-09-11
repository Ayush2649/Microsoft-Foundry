import os

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
api_key = os.environ["AZURE_OPENAI_API_KEY"]

model=ChatOpenAI(
    base_url=endpoint,
    model=deployment_name,
    api_key=api_key,
)

@tool
def get_order_status(order_id: str) -> str:
    """Get the current status of a Cloudxeus order by its ID."""
    orders = {
        "ORD-001": "Dispatched - arriving tomorrow.",
        "ORD-002": "Processing - not yet shipped.",
        "ORD-003": "Delivered on June 12 2026.",
    }
    return orders.get(order_id, f"Order {order_id} not found")

@tool
def get_inventory(product_id: str) -> str:
    """Get the available inventory for a Cloudxeus product by its ID."""
    inventory = {
        "PRD-A1": "142 units in stock.",
        "PRD-B2": "0 units - out  of stock.",
        "PRD-C3": "57 units in stock.",
    }
    return inventory.get(product_id, f"Product {product_id} not found")

agent = create_agent(
    model=model,
    tools=[get_order_status, get_inventory],
    system_prompt="You are a helpful Cloudxeus operations assistant. Use the available tools to answer questions accurately.",
)

response = agent.invoke(
    {
        "messages": [{
            "role": "user",
            "content": "What is the status of order ORD-002 and how many units of PRD-A1 do we have in stock?"
        }]
    }
)

print(response["messages"][-1].content)