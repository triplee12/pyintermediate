from functools import reduce


__author__ = "Ejie Emmanuel Ebuka"

# Lambda

"""
Lambda arguments: is a small anonymous function
"""

product = lambda x: x * x
mult = lambda x,y: x * y
print(product(2))
print(mult(2,23))

addition = lambda y: y + 20
print(addition(20))

divide = lambda x: x / 2
print(divide(200))

my_2D = [(21, 3), (15, 5), (20, 4), (100, 100)]
sort_my_2D = sorted(my_2D, key= lambda x: x[1])
print(sort_my_2D)

my_list = [1, 2, 3, 4, 5]
# map(func, seq)
my_list2 = map(lambda x: x * 2, my_list)
print(list(my_list2))

# filter(func, seq)
my_list3 = filter(lambda x: x % 2 == 0, my_list)
print(list(my_list3))

# WE can do the same like this
a = [y for y in my_list if y % 2 == 0]
print(a)

# reduce(func, seq)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
product_num = reduce(lambda x,y: x*y, num)
print(product_num)
