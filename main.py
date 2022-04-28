import pyautogui
import webbrowser
import time


def open_browser():
    f = open("profile.txt", "r")
    ch = f.readline()
    webbrowser.open(ch)
    f.close

    time.sleep(5)
    xy = pyautogui.locateOnScreen('post.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()

    time.sleep(1)
    xy = pyautogui.locateOnScreen('uploadimg.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()

    time.sleep(1)
    xy = pyautogui.locateOnScreen('show.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()

    time.sleep(1)
    xy = pyautogui.locateOnScreen('path.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')


# pp
open_browser()
