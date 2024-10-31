from pynput.keyboard import *
import colorama
from .colors import *
from .Input import *

colorama.init()

def input(__prompt: str = "", __default: str = "", __colorful: bool = False, __color: None = Color.WHITE) -> str:

    __default += '│'

    print(f"{__prompt}"); print(f"{__color}{__default}", end='\r')

    collect(__default, __color) if __colorful else collect(__default)

    with Listener(on_press=userInput) as listener:
        listener.join()
    
    __default = get(); return __default