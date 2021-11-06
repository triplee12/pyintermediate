__author__ = "Ejie Emmanuel Ebuka"

# Tuples

"""
Tuple is ordered, immutable, and allows duplicate elements
"""
myTuple = ("Ebuka", 28, "Nigeria")
print(myTuple)

myTuple2 = "Ebuka", "28", "Nigeria"
print(myTuple2)

isTuple = ("name") # This is not tuple, but string
print(isTuple)
print(type(isTuple))

isTuple = ("name",) # This is tuple. To return a tuple single tuple element, you have to end it with a comma. 
print(isTuple)
print(type(isTuple))

myTuple3 = tuple(["Ebuka", "28", "Nigeria"]) # We can use tuple function to create a tuple from a list.
print(myTuple3)

# To access elements, we need to refer them by index
item = myTuple[0] # First element at index 0, remember index starts from 0.
print(item)
lastItem = myTuple[-1] # Last element at index -1
print(lastItem)

# To change elements in a tuple
##  myTuple[0] = "Emmanuel" # Oops, this is not possible because tuple is immutable

# Iterating over tuple elements
for e in myTuple:
    print(e)

# Check if element(s) exists in a tuple
if 28 in myTuple:
    print(f'You are {myTuple[1]} years old.')
else:
    print("Oops, I can't find your age.")


# Methods and Functions

# len() method returns the number of items in a tuple.
print(len(myTuple)) # This checks the length of myTuple

# count() method returns the number of occurrences of an item in a tuple and return 0 otherwise.
alphabet = ("a", "b", "c", "d", "e", "f", "g", "a", "a", "c", "b")
print(alphabet.count("a"))

# index() method returns the first index of an element in a tuple
print(alphabet.index("c")) # returns the first occurrence of the element

# convert tuple to list
my_list = list(alphabet)
print(my_list)

# Convert list to tuple
list_to_tuple = tuple(my_list)
print(list_to_tuple)

# Slicing a tuple
sl = alphabet[1:6]
print(sl)

sl1 = alphabet[:8] # This will start from the index 0
print(sl1)

sl2 = alphabet[1:] # This will start from the index 1 to the last index
print(sl2)

sl3 = alphabet[::2] # Returns elements with step of 2
print(sl3)

# Packing and Unpacking
details = "Ebuka", 28, "Abuja" # Packing
name, age, city = details # Unpacking
print(f"name: {name}, age: {age}, city: {city}")