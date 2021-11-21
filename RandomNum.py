import random


__author__ = "Ejie Emmanuel Ebuka"

# Random Numbers

"""
Random Numbers
"""

num = random.random()
print(num)

# This omit the starting and ending values randomly. So it will never return 1 and 100
num2 = random.randrange(1, 100)
print(num2)

# This will include starting and ending values randomly
num3 = random.randint(200, 400)
print(num3)

# Best for statistic, sequence. This will return values between 0 and 1 randomly.
num4 = random.normalvariate(0, 1)
print(num4)

myList = list("abcdefghiklmnopqrstuvwxyz")
# To get random choice from our list, we use random.choice() instead
choice = random.choice(myList)
print(choice)

# If we want to pick more random values, this will never pick an element twice
more = random.sample(myList, 5)
print(more)

# To pick an element twice
twice = random.choices(myList, k=4)
print(twice)

# We can use random.shuffle() to shuffle values
shuffle = random.shuffle(myList)
print(shuffle)
