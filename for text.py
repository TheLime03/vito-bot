# add loop break
from random import randint
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
    xy = pyautogui.locateOnScreen('post.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

    xy = pyautogui.locateOnScreen('hap.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

    pyautogui.write(str(i), interval=0.25)
    time.sleep(1)

    xy = pyautogui.locateOnScreen('share.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()


def refresh():
    xy = pyautogui.locateOnScreen('close.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    open_browser()


# pp
c = 1
open_browser()
while True:
    i = randint(1, 10000000)
    steps()
    c = c+1
    if c == 4:
        c = 1
        refresh()
