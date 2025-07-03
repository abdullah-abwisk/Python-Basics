''' map, filter, reduce '''

# map
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(squared) # <map object at 0x0000021D3D3D4A90>
print(list(squared)) # [1, 4, 9, 16, 25]

# map with lambda function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)
print(list(squared)) # [1, 4, 9, 16, 25]

# filter
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5]
even = filter(is_even, numbers)
print(even) # <filter object at 0x0000021D3D3D4A90>
print(list(even)) # [2, 4]

# filter with lambda function
numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even)) # [2, 4]

# filter with lambda function and map
numbers = [1, 2, 3, 4, 5]
even = map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))
print(list(even)) # [4, 16]

# reduce
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
sum = reduce(add, numbers)
print(sum) # 15

# reduce with lambda function
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum) # 15

# reduce with lambda function and map
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print(sum) # 20