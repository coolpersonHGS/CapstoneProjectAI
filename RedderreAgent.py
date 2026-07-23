import os 
import sys
from dotenv import load_dotenv 
from openai import OpenAI


AImood = ""
AITask = ""
AIDifficulty = 0




prompt = """




"""





load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))


response = client.responses.create(
    model="gpt-4.1-mini",
    input= ""
)



while True:
    pass
    #Give AI screenshot
    #Get Reponse
    #react with a window(s) if neccessary