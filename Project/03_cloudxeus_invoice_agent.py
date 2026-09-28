import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, MCPTool

PROJECT_ENDPOINT = os.environ["PROJECT_ENDPOINT"]

AGENT_NAME = "CloudXeus-Invoice-Intelligence-Agent"
DEPLOYMENT_NAME = "gpt-5.4"

SEARCH_SERVICE_ENDPOINT = os.environ["SEARCH_SERVICE_ENDPOINT"]

KNOWLEDGE_BASE_NAME = "kb-cloudxeus-course-project"

PROJECT_CONNECTION_NAME = os.environ["PROJECT_CONNECTION_NAME"]

mcp_endpoint = (
    f"{SEARCH_SERVICE_ENDPOINT}/knowledgebases/{KNOWLEDGE_BASE_NAME}/mcp"
    "?api-version=2026-05-01-preview"
)

client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

knowledge_tool = MCPTool(
    server_label="knowledge-base",
    server_url=mcp_endpoint,
    require_approval="never",
    allowed_tools=["knowledge_base_retrieve"],
    project_connection_id=PROJECT_CONNECTION_NAME
)

agent = client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=(
            "You are the CloudXeus Invoice Intelligence Agent. "
            "Your role is to help internal CloudXeus teams understand customer invoices "
            "and connect invoice line items to official CloudXeus product information. "

            "You will receive invoice data extracted using Azure Content Understanding. "
            "Use the invoice data to identify the customer, invoice number, invoice date, "
            "due date, line items, quantities, unit prices, taxes, and total amount. "

            "Use the knowledge base tool to answer questions about CloudXeus products. "
            "The knowledge base contains official CloudXeus product-sheet content. "

            "When explaining product features, benefits, or product suitability, "
            "you must use the knowledge base tool. "

            "If the knowledge base does not contain enough information to answer, "
            "say that you do not know based on the available product sheets. "

            "If an invoice line item does not clearly match a product in the knowledge base, "
            "say that the product could not be confidently matched. "

            "For finance summaries, focus on invoice number, customer, dates, totals, taxes, "
            "and any product mismatches. "

            "For sales summaries, focus on purchased products, customer value, product benefits, "
            "and recommended follow-up material. "

            "For customer-facing explanations, use clear and simple business language. "
            "Always be professional, concise, and transparent about missing information."
        ),
        tools=[knowledge_tool],

        # The model decides when to call the knowledge base tool.
        tool_choice="auto"
    )
)

print("Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")