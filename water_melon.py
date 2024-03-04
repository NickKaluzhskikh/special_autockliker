import mouse
from time import sleep
from random import random
from random import randrange as rr
import pyautogui as pg
import keyboard
from tkinter.messagebox import askokcancel


do = False
st = True

def touch():
    global do
    do = not do


def e():
    global st
    st = not askokcancel('Bye, bye!', 'Close the program?')


keyboard.add_hotkey('f6', touch)
keyboard.add_hotkey('f7', e)

pos = (1748, 595)

while st:
    sleep(0.06)

    if not do:
        continue

    x = rr(-3, 4)
    y = rr(-3, 4)
    pg.moveTo(pos[0] + x, pos[1] + y)

    mouse.click()
    

# pos = (1740, 618)
