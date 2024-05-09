from dotenv import load_dotenv
import os
import requests
from openai import OpenAI
from pathlib import Path

load_dotenv()

client = OpenAI()

speech_file_path = Path(__file__).parent / "name-your-file.aac"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="alloy",
  input="This is where you place your script."
)

response.stream_to_file(speech_file_path)
