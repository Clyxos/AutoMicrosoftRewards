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
t.sleep(0.3)
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
    t.sleep(0.5)
    print (searches)
    existing=type
else:
    quit("Done! Make sure you got all of your points.")
    