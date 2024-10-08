from exceptions import *
import keyboard

default: str

def userInput(key):
    global default

    if key.name in exceptions:
        pass
    elif key.name == space:
        default += ' '
    elif key.name == backspace:
        default = default[:-1]
        print(' ' * (len(default) + 1), end='\r')
    elif key.name == enter:
        keyboard.unhook_all()
        print("\033[3m\033[32m{}\033[0m".format(default)); print('-' * (len(default) + 1))
    else:
        default += key.name

    print("\033[3m\033[32m{}\033[0m".format(default), end='\r')

def collect(__default: str): global default; default = __default;