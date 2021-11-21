__author__ = "Ejie Emmanuel Ebuka"

# Function Arguments

"""
Function arguments

- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Lacal vs Global arguments
- Parameter passing (by value or by referrence)
"""

# Parameters are the variables that find or use inside parentheses to define a function.
# Arguments are values pass for parameters while passing a function

# Example: 
def print_age(age): # "age" is a parameter for print_age function
    print(age)

print_age(28) # '28' is an argument for print_age function

# Positional arguments and keyword arguments
def foo(a, b, c, d):
    print(a, b, c, d)

# arguments
foo(1, 2, 3, 4) # Order of arrangement matters
# keyword arguments
foo(a=1, b=2, c=3, d=4) # Here order of arrangement does not matter. We can call the function like this: foo(c=1, a=2, d=3, b=4) and it reutrns result according to the order of the parameters
foo(c=1, a=2, d=3, b=4)

# Default argument
def ba(age=23): # '23' is a default argument for "age" parameter
    print(age)

# Calling "ba()" function without passing argument will still work
ba()
# Calling "ba()" function with age=40 can still work, calling "ba()" function with string as argument will also work but adding additional value will not work
ba(40) # Will work fine
ba("Chris") # Will work too
# ba("Bob", "Chris") # Will not work. TypeError

# Variable-length arguments and keyword arguments
def names(a, b, *args, **kwargs): # Have star *args and double star **kwargs
    # *args means you can pass any number of arguments to a function
    # **kwargs means you can pass any number of keyword arguments to a function
    print(a, b)
    # args is tuple inside your function, so you can go over the tuples
    for arg in args:
        print(arg)
    # kwargs is a dictionary inside your function
    for key in kwargs:
        print(key, kwargs[key])

names("Chris", "Bob") # two positional arguments
# I can use as many as args and kwargs I want
names("Chris", "Bob", True, 1, 2, 3, 4, fruit="orange", pet="Cat", title="Developer")
# First it prints two positional arguments, then 5 args and 3 kwargs

# Sometimes you like to have only args and kwargs
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

# foo(1, 2, 3) # This will raise a TypeError due to a missing positional argument last
foo(1, 2, 3, last=5) # After args follows keyword arguments

# Container unpacking into function arguments
def ba(a, b, c,d):
    print(a, b, c, d)

# Let say we have a list, we can easily unpack into a function
my_list = [1, 2, 3, 4]
# Upack into arguments with star (*)
ba(*my_list)
# It can also work with a tuple, the most important thing is that the length of your container must matches the length of parameters
my_tuple = (1, 2, 3, 4)
ba(*my_tuple)
# For dictionary, the keys must have the same name with the function parameters
my_dict = {"a": 1, "b": 2, "c": 3, "d":4}
ba(*my_dict)
# To get the values of my_dict
ba(**my_dict) # use two stars to unpack dictionary value

# Lacal vs Global arguments
def call_name():
    your_name = "Chris" # Local variable
    print(your_name)
    print(name) # We can access a global variable here inside our function
    # But can not access local variables outside our function

name = "Bob" # Global variable
call_name()
# print(your_name) # This will raise NameError, not defined error because we are trying to access a local variable outside our function
# To modify a global variable inside a function then you have to call it with global keyword

def call_name():
    # global name # Uncomment global name 
    your_name = "Chris" # Local variable
    print(your_name)
    # your_name = name # This will raise UnboundLocalError: local variable 'name' referenced before assignment
    # To avoid UnboundLocalError, use global keyword
    name = "Jennifer"
    print(name)

call_name()
print(name) # We can now access the name variable directly outside our function

# Parameter passing (by value or by referrence)
# There are two rules here:
# The parameter pass in by referrence to object 
# But the referrence pass in by referrence value

# Example
def foo(x):
    x = 1

num = 10
foo(num)
print(num)
