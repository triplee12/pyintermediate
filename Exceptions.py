__author__ = "Ejie Emmanuel Ebuka"

# Errors and Exceptions

"""
Errors and Exceptions: syntax errors, runtime errors...
"""

# Syntax errors are errors thrown by interpreter due to (misspell of words), syntatically incorrect

# Example: a = 2 print(a)


# Exception: even though a program is syntatically correct it may cause an error due to incorrect data types
# Example:

# a = 2 / 0
# print(a)


# Raising an exception
num = 6
if num < 0:
    raise Exception("num should be positive")

# How to handle exceptions

try:
    name = "a" / 2
except Exception as e:
    print(e)


try:
    div = 10 / 0
except ZeroDivisionError as e:
    print(e) # If in anyway there's ZeroDivisionError, this would be execute
except TypeError as e:
    print(e) # If in anyway there's TypeError, this would be execute
else:
    print("We're good to go.") # This line of code only execute when everything is working (no error).
finally:
    print("Execution finished successfully.") # This line of code will always execute

# How t define an exception

class ValueHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    number = 0
    if number > 100:
        print("ValueHighError")
    

def test_ValueHighError(x):
    if x > 100:
        raise ValueHighError("Value is too high", x)

try:
    val = test_ValueHighError(200)
    print(val)
except ValueHighError as e:
    print(f"ValueHighError: {e.message}, Value: {e.value}")

