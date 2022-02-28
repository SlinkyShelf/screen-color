import math
import pyautogui
from PIL import Image
from pynput import keyboard
from pynput.mouse import Controller 

mouse = Controller()

hextable = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def inttohex(int):
    return hextable[math.floor(int/16)]+hextable[int%16]

def on_press(key):
    try:
        if key == keyboard.Key.f9:
            listener.stop()
        if key.char == "s":
            mousex = mouse.position[0]
            mousey = mouse.position[1]
            im = pyautogui.screenshot(region=(mousex,mousey, 1, 1))
            pix = im.load()[0, 0]
            print(pix)
            print("#"+inttohex(pix[0])+inttohex(pix[1])+inttohex(pix[2]))
            print("r =", pix[0])
            print("g =", pix[1])
            print("b =", pix[2])
    except:
        pass

listener = keyboard.Listener(
    on_press = on_press
)
listener.start()
listener.join()