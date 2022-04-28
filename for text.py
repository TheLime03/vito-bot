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


# pp

open_browser()
while True:
    i = randint(1, 10000)
    steps()
