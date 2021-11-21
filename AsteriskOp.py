__author__ = "Ejie Emmanuel Ebuka"

# Asterisk Operator

"""
Asterisk operator can be used in different cases like multiplication, power operation, creation of list or
tuple with repeated elements, args and kwargs parameters, unpacking list,tuple or dictionary into function arguments,
for unpacking containers, matching containers into a list or matching two dictionaries.
"""
# Multiplication
product = 5 * 5
print(product)
# Power
power = 5**5 # Raise 5 to power of 5
print(power)
# List
zeros = [0] * 20 # This will create a list of 20 zeros
print(zeros)
# We can also use tuple
nums = (1, 3) * 10 # This will create a tuple of 10 ones and threes
print(nums)
# It also works with string

# Args and kwargs
def func(a, b, *args, **kwargs):
    print(a, b)
    # args is a tuple
    for arg in args:
        print(arg)
    # kwargs is a dictionary
    for k in kwargs:
        print(k, kwargs[k])

func(2, 3, 4, 34, 42, one=1, five=5)

# Unpacking, important: the number of arguments must match the number of parameters
def foo(a, b, c):
    print(a, b, c)

# List
myList = [1, 2, 3]
foo(*myList) # Unpacking list
# Tuple
myTuple = (1, 2, 3)
foo(*myTuple) # Unpacking tuple
# Dictionary, important: key names must match same function parameter names with the same number of parameters
myDict = {"a": 1, "b": 2, "c": 3}
foo(*myDict) # Unpacking dictionary keys
foo(**myDict) # Unpacking dictionary values

# Merge iterable objects
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7, 8)
new_list = [*my_tuple, *my_list]
print(f"Merged iterable objects from {my_list} and {my_tuple} to {new_list}")
# We can merge set too
my_set = {9, 10, 11, 12}
another_list = [*my_list, *my_tuple, *my_set]
print(another_list)

# Merge dictionaries
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"d": 4, "e": 5, "f": 6}
new_dict = {**dict_1, **dict_2}
print(new_dict)
