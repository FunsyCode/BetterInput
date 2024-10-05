import exceptions
import keyboard

from colorama import just_fix_windows_console

just_fix_windows_console()

default = str

def userInput(key):
    global default

    if key.name in exceptions.exceptions:
        pass
    elif key.name == exceptions.space:
        default += ' '
    elif key.name == exceptions.backspace:
        default = default[:-1]
        print(' ' * (len(default) + 1), end='\r')
    elif key.name == exceptions.enter:
        keyboard.unhook_all()
        print("\033[3m\033[32m{}\033[0m".format(default)); print('-' * (len(default) + 1))
        input(__returnText=default)
    else:
        default += key.name

    print("\033[3m\033[32m{}\033[0m".format(default), end='\r')

def input(__prompt: str = None, __default: str = None, __returnText: str = None):

    if __returnText != None: return __returnText
    global default;
    default = __default

    print(__prompt); print("\033[3m\033[32m{}\033[0m".format(__default), end='\r')

    keyboard.on_press(userInput)
    keyboard.wait()