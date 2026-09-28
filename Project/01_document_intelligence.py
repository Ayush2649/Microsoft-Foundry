# pip install azure.ai.documentintelligence
import os

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential

endpoint = "https://capstone-document-as.cognitiveservices.azure.com/"
key = os.environ["DOCUMENT_INTELLIGENCE_KEY"]

document_url = "https://stcxai103capdeus01.blob.core.windows.net/course-products/student-invoices/CloudXeus_Invoice_INV-CX-2026-1002.pdf"

client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
    api_version="2024-11-30"
)

poller = client.begin_analyze_document(
    model_id="prebuilt-layout",
    body=AnalyzeDocumentRequest(url_source=document_url),
    output_content_format="markdown"
)

result = poller.result()

print(result.content)