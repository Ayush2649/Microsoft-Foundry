import os

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions

CONTENT_SAFETY_ENDPOINT = "https://content-safety-as.cognitiveservices.azure.com/"
CONTENT_SAFETY_KEY = os.environ["CONTENT_SAFETY_KEY"]

endpoint = "https://capstone-document-eus.cognitiveservices.azure.com/"
key = os.environ["DOCUMENT_INTELLIGENCE_KEY"]

document_url = "https://stcxai103capdeus01.blob.core.windows.net/course-products/student-invoices/CloudXeus_Invoice_INV-CX-2026-1001.pdf"

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

document_result = poller.result()

extracted_text = document_result.content

content_safety_client = ContentSafetyClient(
    endpoint=CONTENT_SAFETY_ENDPOINT,
    credential=AzureKeyCredential(CONTENT_SAFETY_KEY)
)

text_request = AnalyzeTextOptions(
    text=extracted_text
)

moderation_result = content_safety_client.analyze_text(text_request)

print("\nContent Safety result:")
should_block = False

for category_result in moderation_result.categories_analysis:
    print(category_result.category, category_result.severity)
if category_result.severity >= 4:
        should_block = True


if should_block:
    print("\nBlocked: unsafe content was detected in the product PDF.")
else:
    print("\nAllowed: the product PDF text can be passed to the agent.")

