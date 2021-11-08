__author__ = "Ejie Emmanuel Ebuka"

# Sets

"""
Sets: sets is unordered, mutable and it does not support duplicates
"""

mySet = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3}
print(mySet)

# We can use set() function to create a set
mySet1 = set([1, 2, 3, 4, 1, 2, 3, 4, 5, 5, 6])
print(mySet1)

emptySet = set() # Empty set

# Functions and Methods

# add() method; use to add a new element to a set
emptySet.add(10)
emptySet.add(20)
emptySet.add(30)
emptySet.add(40)
print(emptySet)

# remove() method; use to remove element from a set
emptySet.remove(40)
print(emptySet)

# discard() method; use to remove element from a set
emptySet.discard(30)
print(emptySet)

# clear() method; use to clear all elements in a set
emptySet.clear()
print(emptySet)

# pop() method; use to remove first element from a set
myPop = mySet.pop()
print(myPop)

# We can iterate over a set using for loop
for e in mySet:
    print(e)

# To check if an element in a set, we can use if statement
if 2 in mySet:
    for e in mySet:
        print(e ** 2)

# Let's talk about union and intersection
evens = {0, 2, 4, 6, 8, 12}
odds = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7, 9, 11}

# Union: combines elements of two sets together without duplications.

union = evens.union(odds)
print(f"Union of {evens} and {odds} is {union}")

# Intersection: only returns elements found in two or more sets
intersect = prime.intersection(evens, odds)
print(f"The intersection of {prime}, {evens} and {odds} is {intersect}") # In this case our set is empty

second_intersect = prime.intersection(evens)
print(f"The intersection of {prime} and {evens} is {second_intersect}") # In this case our set is 2

# Difference; this will return elements not in a set
difference = prime.difference(evens)
print(f"The difference of {prime} and {evens} is {difference}")

# Symmetric_difference; this will return all the difference between two sets
syn_diff = evens.symmetric_difference(prime)
print(syn_diff)

# Functions and Methods

# update() method
prime.update(odds)
print(prime)

# We also have intersection_update
prime.intersection_update(evens)
print(prime)

# difference_update() method
odds.difference_update(evens)
print(odds)

# symmetric_difference_update() method
evens.symmetric_difference_update(prime)
print(evens)

# subset and superset

# subset
print(prime.issubset(evens))
print("__" * 20)
print(odds.issubset(evens))
print("__" * 20)
print(evens.issubset(odds))

# Supperset returns True only if the superset contains all the elements in second set

print("__" * 20)
print(evens.issuperset(prime))

print("__" * 20)
print(odds.issuperset(prime))

print("__" * 20)
print(evens.issuperset(odds))

print("__" * 20)
print(odds.issuperset(evens))

# Disjoint rturns True if setA and setB have no intersection
print("__" * 20)
print(evens.isdisjoint(prime))

# Copy two sets
prime = evens # Wrong
prime.add(10) # This will change original values of evens 
print(prime)
print(evens)

odds = evens.copy() # Right, this will only copy the referrence
odds.add(13)
print(odds)
print(evens)

froze = frozenset([1,2,3,4,5,6,7,8,9]) # Can not be change after creation
print(froze)
# froze.add(10)
# print(froze)