import pyautogui
import time
while True:
    if pyautogui.locateOnScreen('opera.png') != None:
        print("i see you")
        time.sleep(0.5)
    else:
        print("i dont see you")
        time.sleep(0.5)
