__author__ = "Ejie Emmanuel Ebuka"

# Generators

"""
Generators are function that returns an object that can be iterated over.
They generate item one at a time, only when you ask for it.
A generator is like a normal function with yield keyword instead of return keyword.
"""

def myGenerator():
    yield "a"
    yield "b"
    yield "c"
    yield "d"
    yield "e"

gen = myGenerator()
print("-" * 30)
for g in gen:
    print(g)

# We can use next() method to generate a value at a time
# print(next(gen))
# print(next(gen))


def countdown(num):
    print('counting...')
    while num > 0:
        yield num
        num -= 1

count = countdown(10)
print("-" * 30)
for c in count:
    print(c)

# Generator is memory efficient, it saves a lot of memory.

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fibonacci = fib(10)
print("-" * 30)
for f in fibonacci:
    print(f)

# Generator expression

myGen = (g for g in range(11) if g % 2 == 0)
print("-" * 30)
for g in myGen:
    print(g)
