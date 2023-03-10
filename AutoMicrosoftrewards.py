import pyautogui as p
import string as st
import random as r
import time as t
firstsearches=0
searches=int(0)
st.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# This next part of the code is the actual part that types the things into the browser
p.press("win")
p.typewrite("Microsoft Edge")
p.press("Enter")
t.sleep(2)
p.click()
print("Are you ready to begin? Press 1 if so, and put your mouse over the MS edge window.")
temp=input("press 1 when ready ")
t.sleep(2.5)
while searches <= 34:
    newletter=r.choices(st.ascii_letters)
    if searches == 0:
        type=newletter
    else:
        type=newletter+existing
    p.hotkey("ctrl","e")
    p.typewrite(type)
    p.typewrite(["enter"])
    searches += int(1)
    print(searches)
    t.sleep(1)
    existing=type
else:
    quit("Done! Make sure you got all of your points.")
    