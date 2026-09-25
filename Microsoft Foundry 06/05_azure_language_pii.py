from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

import os

endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
api_key = os.environ["AZURE_LANGUAGE_KEY"]

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

documents = [
    "Hi, this is Sarah Chen from Acme Logistics. You can reach me at"
    "sarah.chen@acmelogistics.com or call 123-4567-8901 regarding ticket TKT-1042." 
]

response = client.recognize_pii_entities(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for idx, doc in enumerate(result):
    print(f"--- Document {idx + 1} ---")
    print(f"Redacted text: {doc.redacted_text}")
    print(f"Detected PII entities:")
    for entity in doc.entities:
        print(f" [{entity.category}] '{entity.text}' (confidence: {entity.confidence_score:.2f})")