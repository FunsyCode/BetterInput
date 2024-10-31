# **Easy Input Library (EasyInput)**

The library is distributed under the MIT license and can be downloaded and used by anyone.

----------


## How to install
To install, you can download use pip: `pip install -i https://test.pypi.org/simple/ EasyInput==0.1.5`

Or download library from the repository from [GitHub](https://github.com/FunsyCode/EasyInput.git)

----------

## Using

----------

### Input
The arguments of main functions are:

#### input():
>__prompt: str, __default: str, __colorful: bool, __color: Color or BgColor

- **__prompt:**     `A String, representing a default message before the input.`
- **__default:**    `A String, representing a default message in the input`
- **__colorful:**   `A Bool Variable, representing whether the input will be colored`
- **__color:**      `A Color or BgColor Varible, representing Red, Green and Blue colors in the input`

----------
### Colors

The main classes are:

#### Color
**Color:**       `A Class width many Str Variables,  width ANSI codes of colors`

#### BgColor
**BgColor:**     `A Class width many Str Variables, width ANSI codes of background colors`

----------

The arguments of main function are:

#### coloring():
>__key: dict, __string: str

- **__key:**      `A Dict Variable, in which the key is the word that needs to be colored, and the value is the color. Key of dict, have built-in words like this: __start__, __end__, __mid__, __all__. You can see their in examples`
- **__string**    `A Str Variable, which is the text to be colored`

----------

## Some examples

**Input**
    
    import EasyInput

    EasyInput.input('What's your name? ', 'My name is Funsy')

----------
    
**Color**
  
    from EasyInput import colors
    
    print(colors.coloring({'from': colors.Color.BLUE}, 'Hello from EasyInput!'))
    
    print(colors.coloring({'__start__': colors.BgColor.RED}, 'Hello from EasyInput'))


----------

**Input & Color**
     
    import EasyInput
    
    EasyInput.input('What’s your name? ', 'Funsy', True, EasyInput.colors.Color.BLUE)
