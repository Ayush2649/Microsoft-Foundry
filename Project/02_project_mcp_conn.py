import os

import requests
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

credential = DefaultAzureCredential()

PROJECT_RESOURCE_ID = os.environ["PROJECT_RESOURCE_ID"]

PROJECT_CONNECTION_NAME = "cloudxeus-product-kb-mcp-connection"

SEARCH_SERVICE_ENDPOINT = "https://srch-cloudxeus-ai103-cap-dev-eus-as.search.windows.net"
KNOWLEDGE_BASE_NAME = "kb-cloudxeus-course-project"

mcp_endpoint = (
    f"{SEARCH_SERVICE_ENDPOINT}/knowledgebases/{KNOWLEDGE_BASE_NAME}/mcp"
    "?api-version=2026-05-01-preview"
)

bearer_token_provider = get_bearer_token_provider(
    credential,
    "https://management.azure.com/.default"
)

headers = {
    "Authorization": f"Bearer {bearer_token_provider()}",
    "Content-Type": "application/json"
}

response = requests.put(
    f"https://management.azure.com{PROJECT_RESOURCE_ID}/connections/{PROJECT_CONNECTION_NAME}"
    "?api-version=2025-10-01-preview",
    headers=headers,
    json={
        "name": PROJECT_CONNECTION_NAME,
        "type": "Microsoft.MachineLearningServices/workspaces/connections",
        "properties": {
            "authType": "ProjectManagedIdentity",
            "category": "RemoteTool",
            "target": mcp_endpoint,
            "isSharedToAll": True,
            "audience": "https://search.azure.com/",
            "metadata": {
                "ApiType": "Azure"
            }
        }
    }
)

print(response.status_code)
print(response.text)

response.raise_for_status()

print(f"Connection '{PROJECT_CONNECTION_NAME}' created or updated successfully.")