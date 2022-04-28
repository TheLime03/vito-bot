# add loop break
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
    f1 = open("memespath.txt", "r")
    ch = f1.readline()

    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('delete')
    pyautogui.write(ch, interval=0.1)
    pyautogui.press('enter')


# pp
open_browser()
