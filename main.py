from colorama import just_fix_windows_console
from input import *
import keyboard

just_fix_windows_console()

colorful, color = bool, tuple

def input(__prompt: str = None, __default: str = None, __returnText: str = None):
    if __returnText != None: return __returnText

    print(__prompt); print(__default, end='\r')
    collect(__default)
    keyboard.on_press(userInput)
    keyboard.wait()