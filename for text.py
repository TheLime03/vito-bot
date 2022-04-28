# add loop break
import pyautogui
import webbrowser
import time
import random


def open_browser():
    f = open("profile.txt", "r")
    ch = f.readline()
    webbrowser.open(ch)
    f.close


def steps():
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
    i = random(1, len(list))
    pyautogui.write(l[i], interval=0.25)

    time.sleep(1)
    xy = pyautogui.locateOnScreen('share.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()


# pp
l = [['A pair of cows were talking in the field One says â€œHave you heard about the mad cow disease thatâ€™s going around\n'], ['Yeah the other cow says. â€œMakes me glad Iâ€™m a penguin\n'], ['Once', ' my father came home and found me in front of a roaring fire. That made my father very mad', ' as we didnâ€™t have a fireplaceVictor Borge\n'], ['Your mother has been with us for 20 years said John.Isnt it time she got a place of her own\n'], [
    'â€œMy mother? replied Helen. I thought she was your mother\n'], ['Why donâ€™t pirates take a shower before they walk the plank?\n'], ['They just wash up on shore\n'], ['In Denver', ' the members of a SundayÂ\xad-school class were asked to set down their favorite biblical truths. One youngster laboriously printed: â€œDo one to others as others do one to you. â€”Lee Olson', ' The Denver Post\n'], ['Whatâ€™s the best thing about Switzerland?\n'], ['I donâ€™t know', ' but the flag is a big plus.']]
open_browser()
while True:
    steps()
