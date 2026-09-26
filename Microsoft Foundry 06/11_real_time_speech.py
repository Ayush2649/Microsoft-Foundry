import os

import azure.cognitiveservices.speech as speechsdk

endpoint="https://a75923630-2998-resource.cognitiveservices.azure.com/"
api_key=os.environ["AZURE_SPEECH_KEY"]

speech_config = speechsdk.SpeechConfig(
    subscription=api_key,
    endpoint=endpoint
)

speech_config.speech_recognition_language = "en-IN"

audio_config = speechsdk.audio.AudioConfig(
    use_default_microphone=True
)

recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

def recognizing(evt):
    print("Listening:", evt.result.text)

def recognized(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Final:", evt.result.text)
    elif evt.result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech recognized")

def canceled(evt):
    print("Canceled:", evt)

recognizer.recognizing.connect(recognizing)
recognizer.recognized.connect(recognized)
recognizer.canceled.connect(canceled)

print("🎤 Speak now... Press Ctrl+C to stop.")

recognizer.start_continuous_recognition()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nStopping...")
    recognizer.stop_continuous_recognition()