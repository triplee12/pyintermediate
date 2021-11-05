__author__ = "Ejie Emmanuel Ebuka"

# Lists

"""
Lists: is ordered, mutable and allows duplicate elements.
"""
myList = ["Dog", "Cats", "Pizza"] 
print(f' My lists: {myList}')
# Lists can include number, string, boolean, and unicode.

emptyList = []
print(f' Empty lists: {emptyList}')

myList2 = list("James")
print(f' My second lists: {myList2}')

# List: Indexing; remember index starts from 0

item = myList[0]
print(f' Item: {item}')

# List: Iterating
for i in myList:
    print(f' Iterating: {i}')

# To check if item is in your list, you should use "if"
if "Dog" in myList:
    print(f' Found {myList[0]}')
else:
    print(f'Not Found in {myList}')

# Using append method to add items to the end of the list
myList.append(myList2)
print(myList)

# Using insert method to add items to the list at a given index.
myList.insert(2,"Cake")
print(myList)

# Using pop method to remove the last item from the list
myList.pop()
print(myList)

# Using remove method to remove a specific item from the list
myList.remove("Cake")
print(myList)

# Using remove method to reverse the list
myList.reverse()
print(myList)

# Using sort method to sort list ascending order.
myList.sort()
print(myList)

# Using clear method to remove all items from the list
myList.clear()
print(myList)

# Lists: Slicing lists
numList = [1,2,3,4,5,6,7,8,9,10]
number = numList[2:7] # Specify a starting index for slice and ending index
print(number)
number = numList[:7] # Starting from the beginning
print(number)
number = numList[2:] # Ends to the last element
print(number)

number = numList[::2] # Stepping/skipping
print(number)
number = numList[::-1]
print(number)

# Copying lists
fruits = ["Mango", "Apple", "Banana", "Blueberry"]
fruits_copy = fruits
fruits_copy.append("Orange") # This will modify the original list and the copied list. So be very careful about it.
print(fruits_copy)
print(fruits)

another_copy = fruits.copy() # This will copy the original list of fruits
another_copy.append("Lemon")
print(another_copy)
# We can use list() function and slice [:] to copy a list
# another_copy = list(fruits)
# another_copy = fruits[:]