__author__ = "Ejie Emmanuel Ebuka"

# Strings

"""
Strings: ordered, immutable, text representation. 
A string is produced by using double quotes or single quotes.
"""

myString = "Python programming language"
print(myString)

# We can iterate over the strings with "for" loop

for i in range(len(myString)):
    print(myString[i])

# Functions and Methods

# strip() method is used to remove whites spaces from the string
myString2 = "    Hello, world!   "
print(f"Unstrip string: {myString2}")
myString2 = myString2.strip()
print(f"Strip string: {myString2}")

# upper() method converts a string to upper case
print(f"Upper string: {myString.upper()}")

# lower() method converts a string to lower case
print(f"Lower string: {myString.lower()}")

# startswith() method checks if a string starts with a specific character or word and returns True, otherwise returns False
print(f"Start with string: {myString.startswith('Python')}")

# endswith() method checks if a string ends with a specific character or word and returns True, otherwise returns False
print(f"End with string: {myString.endswith('language')}")

# find() method looks for index of a character and returns '-1' if not found
print(f"Index of 'P' is {myString.find('p')}") # it return index of first character in a string.

# count() method returns the number of a given character in a string and returns '0' if not found.
print(f"Count of 'P' is {myString.count('m')}")

# replace() method replaces a character or word in a string with a new character or word.
print(f"Replace string: {myString.replace('Python', 'python')}")

# split() method splits a string into a list of strings
mylist = myString.split()
print(f"Split string: {myString}")

# join() method joins a list of strings into a single string
newString = " ".join(mylist)
print(f"Join string: {newString}")

# Formatting string
# Old way %, .format()
old = "Python"
old_format = "%s is a programming language" %old
# In "%s" is for string, in "%d" is for integer and "%f" is for float
print("Old way: ", old_format)

old_format2 = "{} is a programming language".format(old)
print("Second old way: ", old_format2)

# New way f-Strings
new_format = f"{old} is a programming language"
print(f"New way: {new_format}")
