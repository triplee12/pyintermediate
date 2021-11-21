from itertools import (product, permutations, combinations, combinations_with_replacement, accumulate, groupby)


__author__ = "Ejie Emmanuel Ebuka"

# Itertools

"""
Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
It is a collection of tools that handle iterators that can be used in a for loops
"""

# Let start with Product
myList1 = [1,2,3,4]
myList2 = [5,6,7,8,] 
prod = product(myList1, myList2)
print(prod) # This will return itertools object
print(list(prod)) # using list function to return the list of products
# We can define number of repeatation
prod = product(myList1, myList2, repeat=3)
print(list(prod))


# Permutations will returns all possible ordering
perm = permutations(myList1)
print(list(perm)) # Using list to print list of permutations
# We can specified number of repeatation in a permutation
perm = permutations(myList1, 3)


# combinations is a function that will all possible combination of list
my_com = [1,2,3,4,5,6]
comb = combinations(my_com, 2)
print(list(comb))
# If you want combination of same number then you can use 'combinations_with_replacement'
comb = combinations_with_replacement(my_com, 3)
print(list(comb))


# accumulate returns the sums of the list
acc = accumulate(myList1)
print(list(acc))


# groupby returns keys from possible iterable list
num = [1, 2, 3, 4, 5, 6, 7]

def products(x):
    return x * x

group_obj = groupby(num, key=products)
for k, v in group_obj:
    print(k, list(v))

# Let group people by age
persons = [{"name": "John", "age":25}, {"name": "James", "age":29},
           {"name": "Jane", "age":25}, {"name": "clara", "age":27}]
persons_obj = groupby(persons, key=lambda x: x["age"])
for k, v in persons_obj:
    print(k, list(v))


# Infinite iterators are count, cycle, repeat
