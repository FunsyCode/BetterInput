# **Better Input Library (BetterInput)** #

The library is distributed under the MIT license and can be downloaded and used by anyone.

----------


## How to install ##
To install, you can use the command:

    pip install BetterInput

Or download from the repository from [GitHub](https://github.com/FunsyCode/BetterInput.git)

----------

## Using ##
### Input
The arguments are:
>__prompt: str, __default: str, __colorful: bool, __color: (red, green, blue)

- **__prompt:**     `A String, representing a default message before the input.`
- **__default:**    `A String, representing a default message in the input`
- at work: **__colorful:**   `A Bool Variable, representing whether the input will be colored`
- at work: **__color:**      `A Tuple Varible, representing Red, Green and Blue colors in the input`


----------
## Some examples ##
**Imports**

    import BetterInput

**Example**
    
    import BetterInput

    BetterInput.input('What's your name? ', 'My name is Funsy', True)


