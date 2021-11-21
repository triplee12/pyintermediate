from collections import ( Counter, namedtuple, OrderedDict, defaultdict, deque)


__author__ = "Ejie Emmanuel Ebuka"

# Collections

"""
Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
The collection module is a special container data types that provide alternatives
for additional functionality compare to general built-in containers
like dictionaries, lists or tuple tuples.
"""
# Let start with the Counter collection

"""
Counter is a container that stores a dictionary keys and count as dictionary values
"""
cout = "aaaabbbbbbbbbcccc"
myCounter = Counter(cout)
print(myCounter)
# We can print the counter keys
print(myCounter.keys())
# We can print the counter values
print(myCounter.values())

# most_common() method returns most common items in a counter collection.
print(myCounter.most_common(1))

# elements() method returns iterable objects
print(myCounter.elements()) # iterable objects
print(list(myCounter.elements())) # using "list" function to create a list of elements


# namedtuple
"""
Namedtuple is a way to create a tuple object data type container
"""

Point = namedtuple('Point', 'x,y')
point = Point(5, 10)
print(point)


# OrderedDict
"""
OrderedDict is like a regular dictionary but it remembers the order of the dictionary was inserted
"""
orderDict = OrderedDict()
orderDict["Apple"] = 5
orderDict["Banana"] = 3
orderDict["Blueberry"] = 7
orderDict["Mango"] = 5
orderDict["Orange"] = 9
print(orderDict)


# Defaultdict
"""
Defaultdict is like regular dictionary container with only difference that it will help create a default key if not provided.
"""
dic = defaultdict(int)
dic["Apple"] = 5
dic["Banana"] = 3
dic["Blueberry"] = 7
dic["Mango"] = 5
dic["Orange"] = 9
print(dic)


# deque
"""
Deque is a double ended queue that can be used to remove items from both ends
"""

deq = deque()
deq.append(2)
deq.append(3)
deq.append(4)
deq.append(5)
deq.append(6)
deq.append(7)
print(deq)

# We can also do appendleft
deq.appendleft(1)
print(deq)

# We can remove items from the deque
deq.pop() # Remove the last element
print(deq)
deq.popleft() # Remove element from left side
print(deq)
deq.clear() # Remove all the elements from the deque
deq.rotate(1) # Rotates element around