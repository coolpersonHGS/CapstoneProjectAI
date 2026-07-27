import subprocess
import sys
import pygame
import math
import psutil
import os
import time
import setproctitle
setproctitle.setproctitle("Redderre_Launcher")
pygame.init()
clock = pygame.time.Clock()

print()
os.chdir(os.getcwd() + '/pythonprojectparts')

#--------------------------------------------------------------------------------------
#--------------------------------- Global Variables -----------------------------------
#--------------------------------------------------------------------------------------

AImood = ""
focustask = ""
AIDifficulty = -1



ActiveScreen = "mainmenu"
NoDistractionPrompt = ""
ActiveTextBox = ""


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
#--------------------------------- Image Loading --------------------------------------
#--------------------------------------------------------------------------------------
Icon = pygame.image.load('RedderreLogo2.png')
Decor = pygame.image.load("Redderre_Decoration.png")
Decor.set_alpha(100)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
#---------------------------------Initialization---------------------------------------
#--------------------------------------------------------------------------------------

RederreWindow = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Redderre Launcher")
pygame.display.set_icon(Icon)


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
#--------------------------------------- Classes --------------------------------------
#--------------------------------------------------------------------------------------





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
        RederreWindow.blit(self.surfaceobj, (self.PositionX, self.PositionY))
        

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

            RederreWindow.blit(self.surfaceobj, (self.PositionX, self.PositionY))

            stringsplit = [self.DisplayStr[i:i + charactersperline] for i in range(0, len(self.DisplayStr), charactersperline)] #["helloia", "hi", "whatsup"]
            
        
        

            for index in range(min(len(stringsplit), int(self.surfaceobj.get_rect().h / (fontH * 0.5)))):
                text_surface = normal_font.render(stringsplit[index], True, pygame.Color("blue"))
                RederreWindow.blit(text_surface, (self.PositionX, self.PositionY + (fontH * 0.6 * index) ) )



class TextInputBox(VisualButtonElement):
    def __init__(self):
        VisualName : str = ""
        FontSize : int = 0
        PositionX : int = 0
        PositionY : int = 0
        surfaceobj : pygame.Surface
        DisplayStr : str = ""

    def Render(self):
        normal_font = pygame.font.SysFont("monospace", self.FontSize)
        fontH, fontW = normal_font.size("word") #height and width
        fontW *= 0.6
        charactersperline = int(self.surfaceobj.get_rect().width / fontW)
        
        linecount = max(1, int(math.ceil(len(self.DisplayStr) / charactersperline)))

        RederreWindow.blit(self.surfaceobj, (self.PositionX, self.PositionY))

        stringsplit = [self.DisplayStr[i:i + charactersperline] for i in range(0, len(self.DisplayStr), charactersperline)] #["helloia", "hi", "whatsup"]
        
       
       

        for index in range(min(len(stringsplit), int(self.surfaceobj.get_rect().h / (fontH * 0.5)) )):
            text_surface = normal_font.render(stringsplit[index], True, pygame.Color("blue"))
            RederreWindow.blit(text_surface, (self.PositionX, self.PositionY + (fontH * 0.6 * index) ) )

       

defaultnull = TextInputBox()
defaultnull.VisualName = "NULL"
defaultnull.DisplayStr = ""



mainmenu : list[VisualButtonElement] = []       # "mainmenu"
normalsettings : list[VisualButtonElement] = [] # "normalsettings"
customization : list[VisualButtonElement] = []  # "customization"

#--------------------------------------------------------------------------------------
#------------------------------------ Element Init ------------------------------------
#--------------------------------------------------------------------------------------


#main menu
CoolIcon = VisualButtonElement()
CoolIcon.surfaceobj = pygame.image.load('RedderreLogo2.png').convert_alpha()
CoolIcon.surfaceobj = pygame.transform.smoothscale(CoolIcon.surfaceobj, (200, 200))
CoolIcon.PositionX = 50
CoolIcon.PositionY = 50
CoolIcon.VisualName = "oi oi"
mainmenu.append(CoolIcon)
normalsettings.append(CoolIcon)
customization.append(CoolIcon)







#CustomizeButton = VisualButtonElement()
#CustomizeButton.surfaceobj = pygame.image.load('Customization.png').convert_alpha()
#CustomizeButton.surfaceobj = pygame.transform.smoothscale(CustomizeButton.surfaceobj, (80, 50))
#CustomizeButton.PositionX = 500
#CustomizeButton.PositionY = 400
#CustomizeButton.VisualName = "customization"
#mainmenu.append(CustomizeButton)


SettingsButton = VisualButtonElement()
SettingsButton.surfaceobj = pygame.image.load('AI_settings2!!!!.png').convert_alpha()
SettingsButton.surfaceobj = pygame.transform.smoothscale(SettingsButton.surfaceobj, (80, 50))
SettingsButton.PositionX = 600
SettingsButton.PositionY = 400
SettingsButton.VisualName = "settings"
mainmenu.append(SettingsButton)

LaunchButton = VisualButtonElement()
LaunchButton.surfaceobj = pygame.image.load('launch_button.png').convert_alpha()
LaunchButton.surfaceobj = pygame.transform.smoothscale(LaunchButton.surfaceobj, (80, 50))
LaunchButton.PositionX = 700
LaunchButton.PositionY = 400
LaunchButton.VisualName = "launch"
mainmenu.append(LaunchButton)

shutdownbutton = VisualButtonElement()
shutdownbutton.surfaceobj = pygame.image.load('close_button.png').convert_alpha()
shutdownbutton.surfaceobj = pygame.transform.smoothscale(shutdownbutton.surfaceobj, (80, 50))
shutdownbutton.PositionX = 700
shutdownbutton.PositionY = 300
shutdownbutton.VisualName = "shutdown"
mainmenu.append(shutdownbutton)



# settings

BackButton = VisualButtonElement()
BackButton.surfaceobj = pygame.image.load('back_button.png').convert_alpha()
BackButton.surfaceobj = pygame.transform.smoothscale(BackButton.surfaceobj, (80, 50))
BackButton.PositionX = 100
BackButton.PositionY = 400
BackButton.VisualName = "back"
normalsettings.append(BackButton)


strictnessInputLabel = VisualTextElement()
strictnessInputLabel.surfaceobj = pygame.Surface((250, 20), pygame.SRCALPHA)
strictnessInputLabel.surfaceobj.fill((0, 0, 0, 0))
strictnessInputLabel.PositionX = 500
strictnessInputLabel.DisplayStr = "Level of strictness (1-10)"
strictnessInputLabel.FontSize = 15
strictnessInputLabel.PositionY = 400
strictnessInputLabel.VisualName = "label"
normalsettings.append(strictnessInputLabel)

strictnessTaskInput = TextInputBox()
strictnessTaskInput.surfaceobj = pygame.Surface((250, 30))
strictnessTaskInput.surfaceobj.fill((200, 20, 20))
strictnessTaskInput.FontSize = 10
strictnessTaskInput.PositionX = 500
strictnessTaskInput.PositionY = 415
strictnessTaskInput.DisplayStr = "Enter a level of strictness"
strictnessTaskInput.VisualName = "strictnessinput"
normalsettings.append(strictnessTaskInput)







PersonalityInputLabel = VisualTextElement()
PersonalityInputLabel.surfaceobj = pygame.Surface((350, 20), pygame.SRCALPHA)
PersonalityInputLabel.surfaceobj.fill((0, 0, 0, 0))
PersonalityInputLabel.PositionX = 500
PersonalityInputLabel.DisplayStr = "AI behavior:"
PersonalityInputLabel.FontSize = 15
PersonalityInputLabel.PositionY = 50
PersonalityInputLabel.VisualName = "label"
normalsettings.append(PersonalityInputLabel)

PersonalityTaskInput = TextInputBox()
PersonalityTaskInput.surfaceobj = pygame.Surface((200, 80))
PersonalityTaskInput.surfaceobj.fill((200, 20, 20))
PersonalityTaskInput.FontSize = 10
PersonalityTaskInput.PositionX = 500
PersonalityTaskInput.PositionY = 70
PersonalityTaskInput.DisplayStr = "Enter a mood for the AI! (Ex: 'Calm')"
PersonalityTaskInput.VisualName = "personalityinput"
normalsettings.append(PersonalityTaskInput)


InputLabel = VisualTextElement()
InputLabel.surfaceobj = pygame.Surface((350, 20), pygame.SRCALPHA)
InputLabel.surfaceobj.fill((0, 0, 0, 0))
InputLabel.PositionX = 500
InputLabel.DisplayStr = "Your focus:"
InputLabel.FontSize = 15
InputLabel.PositionY = 250
InputLabel.VisualName = "label"
normalsettings.append(InputLabel)

TaskInput = TextInputBox()
TaskInput.surfaceobj = pygame.Surface((200, 80))
TaskInput.surfaceobj.fill((200, 20, 20))
TaskInput.FontSize = 10
TaskInput.PositionX = 500
TaskInput.PositionY = 280
TaskInput.DisplayStr = "Enter what you will be focusing  on here! (Ex: 'I want to focus on my homework')"
TaskInput.VisualName = "taskinput"
normalsettings.append(TaskInput)





#customization

BackButton2 = VisualButtonElement()
BackButton2.surfaceobj = pygame.image.load('back_button.png').convert_alpha()
BackButton2.surfaceobj = pygame.transform.smoothscale(BackButton2.surfaceobj, (80, 50))
BackButton2.PositionX = 100
BackButton2.PositionY = 400
BackButton2.VisualName = "back"
customization.append(BackButton2)




#--------------------------------------------------------------------------------------
#------------------------------------- Functions --------------------------------------
#--------------------------------------------------------------------------------------


def Buttonclicked(Buttonname):
    global ActiveScreen
    global ActiveTextBox
    global AImood
    global focustask
    global AIDifficulty

    if(Buttonname == "taskinput"):
        ActiveTextBox = "taskinput"
        if(TaskInput.DisplayStr == "Enter what you will be focusing  on here! (Ex: 'I want to focus on my homework')"):
            TaskInput.DisplayStr = ""
    if(Buttonname == "personalityinput"):
        ActiveTextBox = "personalityinput"
        if(PersonalityTaskInput.DisplayStr == "Enter a mood for the AI! (Ex: 'Calm')"):
            PersonalityTaskInput.DisplayStr = ""
    if(Buttonname == "strictnessinput"):
            ActiveTextBox = "strictnessinput"
            if(strictnessTaskInput.DisplayStr == "Enter a level of strictness"):
                strictnessTaskInput.DisplayStr = ""
    elif (Buttonname == "back"):
        ActiveScreen = "mainmenu"
    elif(Buttonname == "launch"):
        if(AImood != "" and focustask!= "" and AIDifficulty > 0 ):
            try:
                open("PIDinfo.txt")
            except:
                open("PIDinfo.txt", "w")
            foundpid : int = -1

            try:
                foundpid = int(open("PIDinfo.txt").read())
            except:
                pass
            
            if not psutil.pid_exists(foundpid): #No content in the file; no agent is running, so we can create one
                process = subprocess.Popen(
                            [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "RedderreAgent.py"), AImood,   focustask.lower(), str(AIDifficulty) ],
                            stdout=subprocess.DEVNULL,  
                            stderr=subprocess.DEVNULL, 
                            stdin=subprocess.DEVNULL,  
                            start_new_session=True,      
                            cwd=os.path.dirname(os.path.abspath(__file__))
                        )
                print("launching...")
                with open("PIDinfo.txt", "w") as data: # store the PID
                    data.write(str(process.pid))
                    data.close()
                    print("wrote to file")
        else:
            warnpopup = VisualButtonElement()
            warnpopup.surfaceobj = pygame.image.load('warnpopup.png').convert_alpha()
            warnpopup.surfaceobj = pygame.transform.smoothscale(warnpopup.surfaceobj, (50, 50))
            warnpopup.PositionX = 570
            warnpopup.PositionY = 380
            warnpopup.VisualName = ""
            mainmenu.append(warnpopup)
            #print("Missing content" + AImood + focustask)
                    
    elif(Buttonname == "shutdown"):

        test = open("PIDinfo.txt", "r")
        try:
            test.read()
        except:
            open("PIDinfo.txt", "w")
        test.close()
       

        foundpid : int = -1

        try:
            foundpid = int(open("PIDinfo.txt").read())
        except:
            pass

        
        try:
            if psutil.pid_exists(foundpid):
                process = psutil.Process(foundpid)
                process.kill()
                print("attempted termination")
        except:
            pass

        dataw = open("PIDinfo.txt", "w")
        dataw.write("")
        dataw.close()
            
    
    elif (Buttonname == "settings"):
        
            ActiveScreen = "normalsettings"

    elif (Buttonname == "customization"):
        ActiveScreen = "customization"




def ButtonInGroupClicked(mouseX, mouseY, ActivateEvents):
    global ActiveTextBox
    ActiveTextBox = ""
    if(ActiveScreen  == "mainmenu"):
        for element in mainmenu:
            if(element.MouseOver(mouseX, mouseY) ):
                if(ActivateEvents == True):
                    Buttonclicked(element.VisualName)
                return element.VisualName
    elif (ActiveScreen == "customization"):
        for element in customization:
            if(element.MouseOver(mouseX, mouseY) ):
                if(ActivateEvents == True):
                    Buttonclicked(element.VisualName)
                return element.VisualName
    elif (ActiveScreen == "normalsettings"):
        for element in normalsettings:
            if(element.MouseOver(mouseX, mouseY) ):
                if(ActivateEvents == True):
                    Buttonclicked(element.VisualName)
                return element.VisualName


def RenderCurrentScreen():
    if(ActiveScreen  == "mainmenu"):
        for element in mainmenu:
            element.Render()
              
    elif (ActiveScreen == "customization"):
        for celement in customization:
            celement.Render()
    elif (ActiveScreen == "normalsettings"):
        for nelement in normalsettings:
            nelement.Render()



def GetTextBoxFromName(name):
    for TextElm in mainmenu:
        if TextElm.VisualName == name and isinstance(TextElm, TextInputBox):

            return TextElm
    for TextElm2 in customization:
        if TextElm2.VisualName == name and isinstance(TextElm2, TextInputBox):

            return TextElm2
    for TextElm3 in normalsettings:
        if TextElm3.VisualName == name and isinstance(TextElm3, TextInputBox):
    
            return TextElm3
    print(f"No textbox with name {name} found.")
    return defaultnull


    

















#--------------------------------------------------------------------------------------
#---------------------------------   Main Loop  ---------------------------------------
#--------------------------------------------------------------------------------------
LauncherRunning = True

while LauncherRunning:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            LauncherRunning = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if(ActiveTextBox == "taskinput"):
                        focustask = GetTextBoxFromName("taskinput").DisplayStr
                if(ActiveTextBox == "personalityinput"):
                        AImood = GetTextBoxFromName("personalityinput").DisplayStr

                if(ActiveTextBox == "strictnessinput"):
                                    value : int = -1
                
                                    try:
                                        value = int(GetTextBoxFromName("strictnessinput").DisplayStr)
                                    except:
                                        pass
                                    if value != -1:
                                        if(value < 1):
                                            value = 1
                                        if(value > 10):
                                            value = 10
                
                                    AIDifficulty = value
                result = ButtonInGroupClicked(event.pos[0], event.pos[1], True)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if(ActiveTextBox == "taskinput"):
                    focustask = GetTextBoxFromName("taskinput").DisplayStr
 
                if(ActiveTextBox == "personalityinput"):
                    AImood = GetTextBoxFromName("personalityinput").DisplayStr

                if(ActiveTextBox == "strictnessinput"):
                    value : int = -1

                    try:
                        value =  int(GetTextBoxFromName("strictnessinput").DisplayStr)
                    except:
                        pass
                    if value != -1:
                        if(value < 1):
                            value = 1
                        if(value > 10):
                            value = 10

                    AIDifficulty = value
                    print(AIDifficulty)
                   


               
                ActiveTextBox = ""
                
                
            if event.key == pygame.K_BACKSPACE and ActiveTextBox != "":
                SmallerText = GetTextBoxFromName(ActiveTextBox).DisplayStr[:-1]
                GetTextBoxFromName(ActiveTextBox).DisplayStr = SmallerText
               
            
            else: 
                GetTextBoxFromName(ActiveTextBox).DisplayStr += event.unicode

    #
    
    RederreWindow.fill((200, 80, 80))
    RederreWindow.blit(Decor, (0,0))
    RenderCurrentScreen()
    pygame.display.flip()
    pygame.time.wait(20)
pygame.quit()
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

