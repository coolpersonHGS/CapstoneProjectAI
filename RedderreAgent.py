import base64
import os 
from io import BytesIO
import sys
import pygame
from pygame._sdl2 import Window, Renderer
import mss
from Cocoa import NSApp
import tkinter
import math
from PIL import Image
from dotenv import load_dotenv 
from openai import OpenAI
import setproctitle
setproctitle.setproctitle("Redderre_Agent")












CurrentScreenImage : mss.ScreenShot

AImood = "" #calm"
AITask = ""#"Doing Math Homework"
AIDifficulty = 0 # 5
#argument 0 is script name, kinda useless ngl
if( len(sys.argv) > 3):
    AImood = sys.argv[1]   # argument 1, AI's mood
    AITask = sys.argv[2]   # argument 2, AI's anti-distraction task
    AIDifficulty = int(sys.argv[3]) #argument 3, difficulty
    AITask = AITask.replace("_", " ")
else:
    pass
 #   print("Invalid Command Line Arguments")
 #  sys.exit()

#os.environ['SDL_VIDEO_WINDOW_ALWAYS_ON_TOP'] = '1'
pygame.init()
Icon = pygame.image.load('RedderreLogo2.png')
#FunnyDude =
FunnyDude = pygame.display.set_mode((500, 500), flags=pygame.HIDDEN)
pygame.display.set_caption("RedderreAgent")
pygame.display.set_icon(Icon)




class VisualButtonElement:
    def __init__(self):
        VisualName : str = ""
        PositionX : int = 0
        PositionY : int = 0
        surfaceobj : pygame.Surface
   

    def setPos(self, x, y):
        self.PositionX = x
        self.PositionY = y
    
    def Render(self):
        FunnyDude.blit(self.surfaceobj, (self.PositionX, self.PositionY))
        

    def MouseOver(self, MouseX, MouseY):
        objrect : pygame.Rect = self.surfaceobj.get_rect(topleft=(self.PositionX, self.PositionY))
        return objrect.collidepoint(MouseX, MouseY)
    

class VisualTextElement(VisualButtonElement): #this MIGHT be a copy paste bruv
    def __init__(self):
        VisualName : str = ""
        PositionX : int = 0
        PositionY : int = 0
        surfaceobj : pygame.Surface
        FontSize : int = 0
        DisplayStr : str = ""

    def Render(self):
            
            normal_font = pygame.font.SysFont("monospace", self.FontSize)

            fontH, fontW = normal_font.size("word") #height and width
            fontW *= 0.6
            charactersperline = int(self.surfaceobj.get_rect().width / fontW)
            
            linecount = max(1, int(math.ceil(len(self.DisplayStr) / charactersperline)))

            FunnyDude.blit(self.surfaceobj, (self.PositionX, self.PositionY))

            stringsplit = []#[self.DisplayStr[i:i + charactersperline] for i in range(0, len(self.DisplayStr), charactersperline)] #["helloia", "hi", "whatsup"]

            SpaceSplitMessage = self.DisplayStr.split(" ")
            currentword = 0
            
            while(currentword < len(SpaceSplitMessage)):
                AppendString = ""
                CurrentCharCount = 0
                while(currentword < len(SpaceSplitMessage) and CurrentCharCount + len(SpaceSplitMessage[currentword]) < charactersperline):
                    
                    AppendString += SpaceSplitMessage[currentword]
                    AppendString += " "
                    CurrentCharCount += len(SpaceSplitMessage[currentword])
                    currentword += 1
                   
                stringsplit.append(AppendString)
                
        

            for index in range(min(len(stringsplit), int(self.surfaceobj.get_rect().h / (fontH * 0.5)))):
                text_surface = normal_font.render(stringsplit[index], True, pygame.Color("black"))
                FunnyDude.blit(text_surface, (self.PositionX, self.PositionY + (fontH * 0.6 * index) ) )





Cooldude = VisualButtonElement()
Cooldude.surfaceobj = pygame.image.load('RedderreLogo2.png').convert_alpha()
Cooldude.surfaceobj = pygame.transform.smoothscale(Cooldude.surfaceobj, (255, 255))
Cooldude.PositionX = 50
Cooldude.PositionY = 250
Cooldude.VisualName = "oi oi"

MessageLabel = VisualTextElement()
MessageLabel.surfaceobj = pygame.Surface((200, 250))
MessageLabel.surfaceobj.fill((255, 255, 255))
MessageLabel.PositionX = 250
MessageLabel.PositionY = 100
MessageLabel.DisplayStr = "Placeholder"
MessageLabel.FontSize = 20
MessageLabel.VisualName = "label"



#facewindow = Window("face", size=(500, 500), position=(100, 100))
#facerender = Renderer(facewindow)
#messagewindow = Window("message", size=(600, 100), position=(150, 100))
#messagerender = Renderer(messagewindow)

Distracted = False




AIprompt = f"""
You are a helpful and AI that helps people detect when they are distracted from their given task, and supportively encourages them to get back on track. 
Your current mood for encouraging response is "{AImood}" but feel free to make it seem harsh as needed. The users given task that they want to positively focus on is "{AITask}". You should have a { AIDifficulty-2 if Distracted else AIDifficulty}
out of 10 level of strictness when detecting if the user is distracted or off track. The attached image is a .jpg image of the User's current screen. For browsers, focus on thier current tab, rather than every tab in their tab bar.
Based on the aforementioned strictness level and criteria, determine if they are at least 40% off track or distracted. When determining this, ignore any moderately large mostly blank windows, and always assume that they are NOT a distraction and do not hinder focus.
 respond with this EXACT format, without any new line characters, but a singular space between each section:
  < 1 or 0, where 1 is they are distracted and 0 meaning they are not. Ignore the rest of the prompt if this is 0.> <IF DISTRACTED: short and encouraging 1 sentence message to get them back on track, with the message being personalized based off the user's current screen. Replace any spaces with underscores for this specific section, and feel free to use punctuation. Remember, messages should be persuasive rather than aggressive>
 <IF DISTRACTED: where you would want an image of you to appear on the screen horizontally between 0 and 100, where 0 is the left most part of the screen >
 <IF DISTRACTED: where you would want an image of you to appear on the screen vertically between 0 and 100, where 0 is the top most part of the screen >




"""





load_dotenv()

client = OpenAI()


Running = True


while Running: #Never stops unless shutdown/launcher request/task manager tomfoolery
    #facerender.present()
    #messagerender.present()
    with mss.MSS() as sct:
        CurrentScreenImage = sct.grab(sct.monitors[1]) # get current image form primary monitor
        PillowFormat = Image.frombytes("RGB", CurrentScreenImage.size, CurrentScreenImage.rgb)

    imagedatabuffer = BytesIO()
    PillowFormat.save(imagedatabuffer, format="JPEG")
    PureimageData = imagedatabuffer.getvalue()
    base64_image = base64.b64encode(PureimageData).decode("utf-8")
        #Give AI screenshot
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
     #Get Response
    responseparts = response.choices[0].message.content.split()
    #print(responseparts)

    #react with a window(s) if neccessary
    if(responseparts[0] == "1" and Distracted == False):
        responseparts[1] = responseparts[1].replace("_", " ")
        Distracted = True
        #        FunnyDude = 
        pygame.display.set_mode((500, 500),flags=pygame.SHOWN)
        from pygame._sdl2.video import Window
        Window.from_display_module().position = ( 3 * int(responseparts[2]), 3 * int(responseparts[3]) )
        pygame.display.set_caption("RedderreAgent")
        pygame.display.set_icon(Icon)
        if sys.platform == "darwin":
            from Cocoa import NSApp
            from AppKit import NSScreenSaverWindowLevel, NSWindowCollectionBehaviorCanJoinAllSpaces
            app = NSApp()
            if app:
                # Safely loop through the Cocoa Window array
                for window in app.windows():
                    # Locate our specific window by its title string
                    if window.title() == "RedderreAgent":
                        # Level 3 forces NSFloatingWindowLevel (keeps it on top)
                        window.setLevel_(NSScreenSaverWindowLevel) 
    
                        window.setCollectionBehavior_(NSWindowCollectionBehaviorCanJoinAllSpaces)
                        
                        break
                        #First time: Create occurance and do stuff
        FunnyDude.fill((200, 80, 80))
        Cooldude.Render()
        MessageLabel.DisplayStr = responseparts[1]
        MessageLabel.Render()
        pygame.display.flip()
            #I take no credit for this cocoa code; it is pure AI
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False


    if((responseparts[0]) == "0" and Distracted == True):
        FunnyDude = pygame.display.set_mode((500, 500),flags=pygame.HIDDEN)
        Distracted = False
        #FunnyDude = pygame.display.quit()
        print("we quit da program")
        
        #Close the window. yeahhhh



    pygame.time.wait(1000)
    
   
   