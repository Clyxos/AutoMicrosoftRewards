from pyautogui import press, typewrite, click, hotkey
from string import ascii_letters as st
from random import choices as r
from time import sleep as t
firstsearches = 0
searches = int(0)
# This next part of the code is the actual part that types the things into the browser
press("win")
typewrite("Microsoft Edge")
press("Enter")
t(2)
click()
print("Are you ready to begin? Press 1 if so, and put your mouse over the MS edge window.")
temp = input("press 1 when ready ")
t(2.5)
while searches <= 34:
    newletter = r(st)
    if searches == 0:
        type = newletter
    else:
        type = newletter+existing
    hotkey("ctrl", "e")
    typewrite(type)
    typewrite(["enter"])
    searches += int(1)
    print(searches)
    t(1)
    existing = type
else:
    quit("Done! Make sure you got all of your points.")
