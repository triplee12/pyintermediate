__author__ = "Ejie Emmanuel Ebuka"

# Dictionary

""" 
Dictionary: Key-Value pairs, Unordered and Mutable.

It is a collection of key-value pairs that each key represents a value.
{key:value}

You can change dictionary keys and values after creation.
"""

myDict = {"firstname": "John", "lastname": "James", "age": 28, "email": "jj@python.com"}
print(f"My details: {myDict}")

# WE can use dict function to create a new dictionary
myDict1 = dict(name = "John", age = 28, email = "jj@python.com")
print(f"My details: {myDict1}")

# To access the dictionary value, we need to use the dictionary key
value = myDict["firstname"]
print(value)

myDict1["pet"] = "Dog"
print(myDict1)

# Functions and Methods

# del method: Delete a given key and it's value from the dictionary
del myDict1["pet"]
print(myDict1)

# pop method: delete a key and it's value from the dictionary
myDict.pop("age")
print(myDict)

# popitem method: delete the last key and it's value from the dictionary'
myDict1.popitem() # Python 3.7+ compatibility
print(myDict1)

# To check if a key is in the dictionary
if "firstname" in myDict:
    print(myDict["firstname"])

# To loop through a dictionary
for k,v in myDict.items():
    print(k, ":", v) # "k" is for key, "v" is for value

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

# When you have to copy a dictionary, you have to be careful
myDict1 = myDict.copy() # Right
print(myDict1)

myDict_cp = myDict # Wrong
myDict_cp["age"] = 28 # This will modify the original copy
print(myDict_cp)
print(myDict)

# update() method
myDict.update(myDict1) # This will modify myDict with myDict1 items
print(myDict)
