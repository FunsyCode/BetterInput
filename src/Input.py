from pynput.keyboard import *
import colorama

from .exceptions import *
from .cursor import *
from .colors import *

default, color = str, None
colorama.init()

def userInput(key) -> bool:
    global default, color; key = '{}'.format(key)
    key = key.replace("'", ''); key = key.replace("'", '')

    if key in exceptions:
        pass
    elif key == space:
        default = Go(default + ' ')
    elif key == backspace:
        default = Backspace(default)
        print(f"{color}{default} ", end='\r')
    elif key == right:
        default = Right(default)
    elif key == left:
        default = Left(default)
    elif key == enter:
        print(f"{color}{default}")
        return False
    else:
        default += key; default = Go(default)

    print(f"{Coloring({'import': color}, default)}", end='\r')

def collect(__default: str, __color: None = Color.WHITE) -> None: global default, color; default = __default; color = __color
def get() -> str: return default