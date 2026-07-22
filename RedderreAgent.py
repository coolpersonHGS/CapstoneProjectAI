import os 
import sys
from dotenv import load_dotenv 
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))


response = client.responses.create(
    model="gpt-4.1-mini",
    input= ""
)