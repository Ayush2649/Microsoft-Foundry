import os

from azure.ai.transcription import TranscriptionClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.transcription.models import TranscriptionOptions, TranscriptionContent

endpoint="https://a75923630-2998-resource.cognitiveservices.azure.com/"
api_key=os.environ["AZURE_SPEECH_KEY"]

client=TranscriptionClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

audio_path="conversation.wav"
with open(audio_path, "rb") as audio_file:
    options=TranscriptionOptions(locales=["en-US"])
    response=client.transcribe(TranscriptionContent(definition=options, audio=audio_file))

print(response.combined_phrases[0].text)
