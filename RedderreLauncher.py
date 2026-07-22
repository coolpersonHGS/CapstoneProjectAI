import subprocess
import sys
import pygame
pygame.init()
clock = pygame.time.Clock()

#--------------------------------------------------------------------------------------
#--------------------------------- Global Variables -----------------------------------
#--------------------------------------------------------------------------------------


normal_font = pygame.font.SysFont("Arial", 40)



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
    
class TextInputBox(VisualButtonElement):
    


    def __init__(self):
        VisualName : str = ""
        PositionX : int = 0
        PositionY : int = 0
        surfaceobj : pygame.Surface
        DisplayStr : str = ""

    def Render(self):
        RederreWindow.blit(self.surfaceobj, (self.PositionX, self.PositionY))
        text_surface = normal_font.render(self.DisplayStr, True, pygame.Color("blue"))
        RederreWindow.blit(text_surface, (self.PositionX, self.PositionY) )

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







CustomizeButton = VisualButtonElement()
CustomizeButton.surfaceobj = pygame.image.load('Customization.png').convert_alpha()
CustomizeButton.surfaceobj = pygame.transform.smoothscale(CustomizeButton.surfaceobj, (80, 50))
CustomizeButton.PositionX = 500
CustomizeButton.PositionY = 400
CustomizeButton.VisualName = "customization"
mainmenu.append(CustomizeButton)


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

# settings

BackButton = VisualButtonElement()
BackButton.surfaceobj = pygame.image.load('back_button.png').convert_alpha()
BackButton.surfaceobj = pygame.transform.smoothscale(BackButton.surfaceobj, (80, 50))
BackButton.PositionX = 100
BackButton.PositionY = 400
BackButton.VisualName = "back"
normalsettings.append(BackButton)



TaskInput = TextInputBox()
#LaunchButton.surfaceobj = pygame.image.load('launch_button.png').convert_alpha()
TaskInput.surfaceobj = pygame.Surface((200, 80))
TaskInput.surfaceobj.fill((200, 0, 0))
TaskInput.PositionX = 500
TaskInput.DisplayStr = ""
TaskInput.PositionY = 200
TaskInput.VisualName = "taskinput"
mainmenu.append(TaskInput)




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
    if(Buttonname == "taskinput"):
        ActiveTextBox = "taskinput"
    elif (Buttonname == "back"):
        ActiveScreen = "mainmenu"
    elif(Buttonname == "launch"):
        print("launching...")
    elif (Buttonname == "settings"):
        
        ActiveScreen = "normalsettings"

    elif (Buttonname == "customization"):
        ActiveScreen = "customization"




def ButtonInGroupClicked(mouseX, mouseY, ActivateEvents):
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
                result = ButtonInGroupClicked(event.pos[0], event.pos[1], True)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               
                ActiveTextBox = ""
                
                
            if event.key == pygame.K_BACKSPACE:
                SmallerText = GetTextBoxFromName(ActiveTextBox).DisplayStr[:-1]
                GetTextBoxFromName(ActiveTextBox).DisplayStr = SmallerText
                print(GetTextBoxFromName(ActiveTextBox).DisplayStr)
            
            GetTextBoxFromName(ActiveTextBox).DisplayStr += event.unicode

            
              
   
    
    RederreWindow.fill((200, 80, 80))
    RederreWindow.blit(Decor, (0,0))
    RenderCurrentScreen()
    pygame.display.flip()
    pygame.time.wait(20)
pygame.quit()
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

