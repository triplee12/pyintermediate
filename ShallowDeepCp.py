import copy


__author__ = "Ejie Emmanuel Ebuka"

# Shallow vs Deep copy

"""
Shallow vs Deep copy

- Shallow copy: one level deep, only referrences of nested objects
- Deep copy: full independent copy
"""
original = 10
copy_o = original # copies original
print(f"Copied: {copy_o}")
copy_o = 20 # This will only modify the copy and not the original
print(f"Modified: {copy_o}")
print(f"Original: {original}")

# Above example can never work for iterable objects
# my_list = [1, 2, 3, 4]
# cp_list = my_list
# print(f"Copied: {cp_list}")
# cp_list[0] = 5 # This will also modify the copy and the original list
# print(f"Modified: {cp_list}")
# print(f"Original: {my_list}")

# To make an actual copy of the list, we need to import copy module
# Shallow copy
my_list = [1, 2, 3, 4]
cpy_list = copy.copy(my_list) # shallow copy
# cpy_list = list(my_list) # this also works (shallow copy)
# cpy_list = my_list.copy() # shallow copy
# cpy_list = my_list[:] # this also works (shallow copy)
cpy_list[0] = 5 # This will modify the copy and not the original list
print(f"Modified: {cpy_list}")
print(f"Original: {my_list}")

# Deep copy
# Nested iterable objects
my_2D = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# cp_2D = copy.copy(my_2D) # this will not work because it is a Shallow copy
# To make a deep copy of our nested iterable objects, we need to use copy.deepcopy()
cp_2D = copy.deepcopy(my_2D)
cp_2D[1][2] = 9
print(f"Modified: {cp_2D}")
print(f"Original: {my_2D}")

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss=None, employee=None):
        self.boss = boss
        self.employee = employee


person_1 = Person("Chris", 28)
# Here we can use shallow copy or deep copy
person_2 = copy.deepcopy(person_1)
person_2.name = "Bobs"
print(f"Modified: {person_2.name}")
print(f"Original: {person_1.name}")

person_3 = Person("Jane", 26)
person_4 = Person("Philip", 35)

company = Company(person_3, person_4)
# Here only deep copy is necessary (can work)
cp_company = copy.deepcopy(company)
cp_company.boss.age = 36
print(f"Modified: {cp_company.boss.age}")
print(f"Original: {company.boss.age}")
