import json
import os

from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput
from azure.ai.projects import AIProjectClient

CONTENT_UNDERSTANDING_ENDPOINT = os.environ["CONTENT_UNDERSTANDING_ENDPOINT"]
CONTENT_UNDERSTANDING_KEY = os.environ.get("CONTENT_UNDERSTANDING_KEY")

ANALYZER_ID = "cloudxeusstudentinvoiceanalyzer"

INVOICE_BLOB_URL = "https://stcxai103capdeus01.blob.core.windows.net/course-products/student-invoices/CloudXeus_Invoice_INV-CX-2026-1003.pdf"

PROJECT_ENDPOINT = "https://clouxeus-capstone-proje-resource.services.ai.azure.com/api/projects/clouxeus-capstone-project"
AGENT_NAME = "CloudXeus-Invoice-Intelligence-Agent"


credential = (
    AzureKeyCredential(CONTENT_UNDERSTANDING_KEY)
    if CONTENT_UNDERSTANDING_KEY
    else DefaultAzureCredential()
)

content_client = ContentUnderstandingClient(
    endpoint=CONTENT_UNDERSTANDING_ENDPOINT,
    credential=credential,
    api_version="2025-11-01"
)

poller = content_client.begin_analyze(
    analyzer_id=ANALYZER_ID,
    inputs=[
        AnalysisInput(url=INVOICE_BLOB_URL)
    ]
)

invoice_result = poller.result()

print("Invoice analysis completed.")

project_client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

openai_client = project_client.get_openai_client()

prompt = f"""
Create a complete invoice intelligence report.

Use the extracted invoice data below.
When you need product information, use the CloudXeus product knowledge base.

Include:
1. Invoice overview
2. Products purchased
3. Product explanations from the knowledge base
4. Product match validation
5. Finance summary
6. Customer-friendly explanation
7. Recommended sales follow-up

Extracted invoice data:
{json.dumps(invoice_result.as_dict(), indent=2)}
"""

response = openai_client.responses.create(
    extra_body={
        "agent_reference": {
            "name": AGENT_NAME,
            "type": "agent_reference"
        }
    },
    input=prompt
)

print("\n----- Agent Report -----\n")
print(response.output_text)