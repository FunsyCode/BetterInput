def Right(text: str) -> str:
    index = text.find('│')
    if index == len(text) - 1: return text
    elif index == -1: return text
    else: text  = (text[:index] + text[index + 1] + '│' + text[index + 2:])
    return text

def Left(text: str) -> str:
    index = text.find('│')
    if index == 0: return text
    elif index == -1: return text
    else: text = (text[:index-1] + '│' + text[index-1] + text[index+1:])
    return text

def Go(text: str) -> str:
    index = text.find('│')
    text = text[:index + 1] + text[-1] + text[index + 1:]; text = text[:-1]
    text = text[:index] + text[index + 1] + text[index] + text[index + 2:]
    return text

def Backspace(text: str) -> str:
    index = text.find('│')
    if index == 0: return text
    else: text = text[:index-1] + text[index] + text[index+1:]
    return text