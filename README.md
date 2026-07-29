# Redderre AI
Final Capstone Project

Redderre runs a background python process that has AI analyze screen data and react accordingly
to stop users from going off task. 


## Setup [REQUIRES MAC OPERATING SYSTEM]

Step 1 [Clone]:  
    Clone The project
    run "git clone <ThisGithubProjectURL>" in your folder directory of choice


Step 2 [Dependencies]:  
    Install Python dependencies (preferably with pip)
        The following are all mandatory depedencies that require installation
                -Dotenv
                -Psutil
                -Pygame
                -SetProctitle
                -Pillow(PIL)
                -MSS
                -OpenAI
                -Cocoa


Step 3 [API]:  
    Obtain a gpt-4.1-mini API key
    Put API key in python .env file


After following all these steps, the project file "RedderreLauncher.py" should run, and be capable of launching "RedderreAgent.py"
The website is not required for any functionaility, and the python does not interact with it whatsoever.


## Project Structure

----------------------------
        main/
            index.html
            script.js
            style.css
            RedderreInstall.dmg (empty placeholder file)
            RedderreLogo2.png(Website asset)
            README.md (Your reading this right now!)
            .gitignore
            .env (Not present, but should be added with a gpt-4.1-mini API key when replicating this project)

                pythonprojectparts/ 
                    RederreLauncher.py (required for launching the agent)
                    RedderreAgent.py (Main AI usage)
                    [REMAINING FILES ARE ASSETS(images) OR NOT REQUIRED FOR REPLICATION]



----------------------------



## Limitations
    -Currently does not working in fullscreen
    -Rarely detects the window itself as a distraction, causing the window to stay untill it takes up
     less screen real estate
    -Does not use continous screen images like a video, treats each image as seperate from any previous.




# Further Information 

## Problem Being Solved:
When work needs to be done online, users often get distracted and go off task, postponing what they need to do. There are no adaptive
methods of accountability to stop people from going off task, other than self motivation and another person literally watching your
 screen constantly. This is a real issue because procrastination (What the user is facing), leads to failure to complete necessary tasks,
  which would in turn lead them to less opportunities in the future.

## AI System Behavior:
While the application is active, it gets an image of the current screen, and has it processed by gpt-4.1-mini. Using a mix of vision,
reasoning over images, and classification, it sends a response to the application detailing whether or not the user is distracted, 
and how. The application interprets the data and reacts, if necessary it will send the user obstructive reminders to stay focused.
 Screen data is not stored or saved in any way, and is purely used to check for distractions.

## Features:
The application can stop the user from getting stuck in distractions. It does so by obnoxiously taking up screen space and giving
the user messages to focus or take a breaker. 

## Tech Stack:
The technologies used in this project are Python programming language and the OpenAI API. Additionally, many 3rd party libraries
are used as well, being Psutil, MSS, Pygame, Pillow, Cocoa, and Setproctitle. 


## Roadmap:  
Early Access launch + Improvements/Bugfixes phase:  
Redderre becomes available and downloadable to the public for free. Feedback will receive more attention in this starting phase.  
 For the week following the initial launch, the team will try to apply the community feedback in order to improve Redderre.  
         _  
         |  
         |  
         v  
Customizability Update:  
A small update that would give users more personalization and customizability for their Redderre agents.  
         _  
         |  
         |  
         v  
Windows support:  
Redderre only supports MacOS. Once Redderre is a more complete product, our next priority would be to ship it to the Windows OS.  
         _  
         |  
         |  
         v  
Official launch:  
After the improvement phase, Redderee would be considered “Complete”. Feedback would be looked at less, and changes would be made slower.  
If the application gained enough traction it would become a service that requires a one time payment. People who installed it before the 
official launch would not need to participate in the one time payment.  


