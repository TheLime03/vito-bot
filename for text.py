# add loop break
import pyautogui
import webbrowser
import time


def open_browser():
    f = open("profile.txt", "r")
    ch = f.readline()
    webbrowser.open(ch)
    f.close
    time.sleep(4)


def steps():
    time.sleep(1)
    pyautogui.write(str(i), interval=0.25)
    time.sleep(1)
    xy = pyautogui.locateOnScreen('share.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()


# pp
i = 1
open_browser()
while True:
    steps()
    i = i+1
