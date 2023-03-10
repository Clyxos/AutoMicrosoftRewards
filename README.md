This is a quick and easy python 3.10 script that automatically open edge and searches for you. This is one of my first projects, so it's gonna be really bad. Thanks!
(note: download the .exe file for easy usage)

# Building:

Required Languages: Python

Required Libraries: PyautoGUI

Operating systems supported: Windows (as far as I know)

## How to install PyautoGUI and Pyinstaller:

1. Make sure you have pip installed. This is done by typing pip in the command prompt.
2. For Mac Os and potentially Linux, look at other guides on how to do it since its different from windows.
3. Type into your command line "pip install pyautogui"
4. Repeat these steps for pyinstaller, but instead use the command "pip install pyinstaller"

## The actual building:

1. Open a command prompt in the directory of where it was downloaded to
2. Type "pyinstaller AutoMicrosoftrewards.py --onefile  
   (If this says the command is not recognized, your python PATH variables are messed up. Search up how to put script folder from python into Path)

3. Wait for the process to complete.

4. You should now find a build and dist folder. Open up the dist one and your .exe should be there
