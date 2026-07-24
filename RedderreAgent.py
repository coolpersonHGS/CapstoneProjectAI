import base64
import os 
from io import BytesIO
import sys
import pygame
import mss
from PIL import Image
from dotenv import load_dotenv 
from openai import OpenAI

CurrentScreenImage : mss.ScreenShot

AImood = ""
AITask = ""
AIDifficulty = -1
#argument 0 is script name, kinda useless ngl
if( len(sys.argv) > 3):
    AImood = sys.argv[1]   # argument 1, AI's mood
    AITask = sys.argv[2]   # argument 2, AI's anti-distraction task
    AIDifficulty = int(sys.argv[3]) #argument 3, difficulty
    AITask = AITask.replace("_", " ")
else:
    sys.exit()


print(AImood)
print(AITask)
print(AIDifficulty)


AIprompt = f"""
You are a helpful and AI that helps people detect when they are distracted from their given task, and encourages them to get back on track.
Your current mood for encouraging response is "{AImood}" but feel free to make it seem harsh as needed. The users given task that they want to positively focus on is "{AITask}". You should have a {AIDifficulty}
out of 10 level of strictness when detecting if the user is distracted or off track. The attached image is a .jpg image of the User's current screen.

Based on the aforementioned strictness level and criteria, determine if they are at least 40% off track or distracted. respond with "1" if they are, and "0" if they are not.
Afterwards, on the next line, state why you chose your given output.



"""





load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))






#while True: #Never stops unless shutdown/launcher request/task manager tomfoolery
with mss.MSS() as sct:
    CurrentScreenImage = sct.grab(sct.monitors[1]) # get current image form primary monitor
    PillowFormat = Image.frombytes("RGB", CurrentScreenImage.size, CurrentScreenImage.rgb)

imagedatabuffer = BytesIO()
PillowFormat.save(imagedatabuffer, format="JPEG")
PureimageData = imagedatabuffer.getvalue()
base64_image = base64.b64encode(PureimageData).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": f"{AIprompt}"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "auto"
                    }
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)
#Give AI screenshot
#Get Reponse
#react with a window(s) if neccessary