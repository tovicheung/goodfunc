# goodfunc
A random module I made to declutter Python functions!
(This is only proof-of-concept, and made for fun)

# Setup
Put goodfunc.py at the same directory as your script

# Usage - Simple functions
For example I have the following code
```
def ansi_red(text):
    return f"\033[31m{text}\033[0m"

def ansi_bold(text):
    return f"\033[1m{text}\033[0m"

def ansi_italic(text):
    return f"\033[3m{text}\033[0m"

def ansi_underline(text):
    return f"\033[4m{text}\033[0m"
```
Running `print(ansi_red(ansi_bold(ansi_italic(ansi_underline("hi")))))` will result in printing "hi" in red, bold, italic and underline

Using this module, we can modify our code to
```
from goodfunc import goodfunc

@goodfunc
def ansi_red(text):
    return f"\033[31m{text}\033[0m"

@goodfunc
def ansi_bold(text):
    return f"\033[1m{text}\033[0m"

@goodfunc
def ansi_italic(text):
    return f"\033[3m{text}\033[0m"

@goodfunc
def ansi_underline(text):
    return f"\033[4m{text}\033[0m"
```
So now I can run `print("hi" | ansi_red | ansi_bold | ansi_italic | ansi_underline)` to get the same result!
(I can still use the original code)

# Usage - multiple arguments
There's currently only little support for multiple arguments
```
@goodfunc
def foo(arg1, arg2): ...
```
Running `foo(1, 2)` is the same as `(1, 2) | foo`

Tuple detection is included, so if the function only accepts one argument, but a tuple is passed in, it will pass the entire tuple as one argument
