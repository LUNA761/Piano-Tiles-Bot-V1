'''
AUTO PIANO TILES V1.5 (by LUNA#6969 (discord) dm me for any help))

varibles:

delay - the delay between clicks
black - the rgb code for the black box

requirements:

pyautogui
pywin32
pillow

these will automaticly be installed at start
'''







import os

e = ["pyautogui", "pywin32", "pillow"]

for x in e:
    os.system(f"pip install {x}")

import pyautogui, time, ctypes, threading, win32api, keyboard, webbrowser
from PIL import ImageGrab
from tkinter import *


delay = 0.02 # CHANGE THIS TO YOUR LIKEING -  i suggest a delay speed of about 0.02 to 0.04


black = (17, 17, 17) # DO NOT change this unless you dm me asking what it does




places = {} # a dict to store x and y data

def mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def app():
    mbox("Piano Tiles Bot", "After clicking ok you will have 3 seconds to get ready. Hold Q anytime to stop", 0)
    time.sleep(3)
    threading.Thread(target=appthread).start()

def appthread():
    while keyboard.is_pressed('q') == False:
        px = ImageGrab.grab().load()
        for y in range(0, 100, 10):
            for x in range(0, 100, 10):
                v1 = px[places["1"]["1"], places["1"]["2"]]
                v2 = px[places["2"]["1"], places["2"]["2"]]
                v3 = px[places["3"]["1"], places["3"]["2"]]
                v4 = px[places["4"]["1"], places["4"]["2"]]
        if v1 == black:
            pyautogui.click(places["1"]["1"], places["1"]["2"])
            time.sleep(delay)
        if v2 == black:
            pyautogui.click(places["2"]["1"], places["2"]["2"])
            time.sleep(delay)
        if v3 == black:
            pyautogui.click(places["3"]["1"], places["3"]["2"])
            time.sleep(delay)
        if v4 == black:
            pyautogui.click(places["4"]["1"], places["4"]["2"])
            time.sleep(delay)

def select4():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row four!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["4"] = {}
    places["4"]["1"] = x
    places["4"]["2"] = y

def select1():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row one!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["1"] = {}
    places["1"]["1"] = x
    places["1"]["2"] = y

def select2():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row two!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["2"] = {}
    places["2"]["1"] = x
    places["2"]["2"] = y

def select3():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row three!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["3"] = {}
    places["3"]["1"] = x
    places["3"]["2"] = y

def select4():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row four!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["4"] = {}
    places["4"]["1"] = x
    places["4"]["2"] = y

def openwebsite():
    webbrowser.open("http://tanksw.com/piano-tiles/")

root = Tk()
root.title("Piano Tiles Bot")
root.geometry("100x160")

Label(root, text="Auto Piano Tiles")

Button(root, text="Open Piano Tiles", command=openwebsite).pack()

Button(root, text="Select Row 1", command=select1).pack()
Button(root, text="Select Row 2", command=select2).pack()
Button(root, text="Select Row 3", command=select3).pack()
Button(root, text="Select Row 4", command=select4).pack()
Button(root, text="Start", command=app).pack()
root.mainloop()
