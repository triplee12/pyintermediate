import functools


__author__ = "Ejie Emmanuel Ebuka"

# Decorators

"""
A decorator is a function that takes another function as an argument and extends the behavior of the function without explicity modify it.
In other words, it allows you to call an existing function in another function without modifying the behavior of the function (decorator).
Decorators: there are two types of decorators; class decorator and function decorator.
"""

# Function decorator

def myDecorator(func): # A decorator most have an inner function that calls and return the inner function. 
    
    @functools.wraps(func) # this will preserve the original function signature
    def start(*args, **kwargs): # Inner function
        print("Start...")
        func(*args, **kwargs) # Function as decorator argument
        print("End...")
    return start


@myDecorator # decorator
def fundeco(): # this function will be extended with the behavior of myDecorator.
    print("My decorator is working...")

test = fundeco()


def my_maths(func):
    
    @functools.wraps(func)  # this will preserve the original function signature
    def addition(*args, **kwargs):
        add = func(*args, **kwargs)
        return add    
    return addition


@my_maths
def solve(a, b):
    print("Solving...")
    return a + b

mt = solve(20, 40)
print(mt)


def repeat(times):
    def repeat_dec(func):
        @functools.wraps(func)  # this will preserve the original function signature
        def mult(*args, **kwargs):
            for i in range(times):
                loop = func(*args, **kwargs)
            return loop
        return mult
    return repeat_dec

@repeat(times = 4)
def greeting(name):
    print(f"Hello {name}")

greeting("Jenny")

# Nested decorators
# You can stack decorators on top of each other


def debug(func):
    @functools.wraps(func)  # this will preserve the original function signature
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__} with signature: ({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned result: {result!r}")
        return result
    return wrapper

@myDecorator
@debug
@repeat(times = 6)
def say_hello(name):
    greet = f"Hello {name}"
    print(greet)
    return greet

say_hello("Philip")


# Class decorators

class MyDecoratorCount:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Executing {self.calls} times")
        return self.func(*args, **kwargs)
    

@MyDecoratorCount
def say_hi():
    print("Hi")

say_hi()
# say_hi()
# say_hi()

