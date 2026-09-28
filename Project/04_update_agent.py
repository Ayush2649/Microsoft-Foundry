from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool

PROJECT_ENDPOINT = (
    "https://clouxeus-capstone-proje-resource.services.ai.azure.com/"
    "api/projects/clouxeus-capstone-project"
)

AGENT_NAME = "CloudXeus-Invoice-Intelligence-Agent"
AGENT_MODEL = "gpt-5.2"

MCP_ENDPOINT = (
    "https://srch-cloudxeus-ai103-cap-dev-eus-as.search.windows.net/"
    "knowledgebases/kb-cloudxeus-course-project/"
    "mcp?api-version=2026-08-01-preview"
)

PROJECT_CONNECTION_NAME = "cloudxeus-iq-connection"

project_client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

instructions = """
You are a helpful invoice intelligence assistant.

Use the CloudXeus product knowledge base whenever product
information or product validation is required.

Use the knowledge base to retrieve relevant product information.

If the knowledge base does not contain the required information,
clearly state that the information was not found.

Provide clear and accurate invoice analysis.
"""

mcp_kb_tool = MCPTool(
    server_label="knowledge-base",
    server_url=MCP_ENDPOINT,
    require_approval="never",
    allowed_tools=["knowledge_base_retrieve"],
    project_connection_id=PROJECT_CONNECTION_NAME
)

agent = project_client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=AGENT_MODEL,
        instructions=instructions,
        tools=[mcp_kb_tool]
    )
)

print("Agent updated successfully!")
print(f"Agent name: {agent.name}")
print(f"Agent version: {agent.version}")