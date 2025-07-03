''' tuples '''

# tuple
# tuple is immutable (values cannot be changed)
tup = (1, 2, 3, 4, 5)
print(tup[0]) # 1
print(type(tup)) # <class 'tuple'>
tup = (1)
print(type(tup)) # <class 'int'>
tup = (1,)
print(type(tup)) # <class 'tuple'>
tup[0] = 2 # TypeError: 'tuple' object does not support item assignment

# tuple methods
# count
tup = (1, 2, 3, 2, 1)
print(tup.count(2)) # 2
# index
tup = (1, 2, 3)
print(tup.index(2)) # 1
# index with start and end
tup = (1, 2, 3, 2, 1)
print(tup.index(2, 2, 5)) # 3
# len
tup = (1, 2, 3)
print(len(tup)) # 3
# max
tup = (1, 2, 3)
print(max(tup)) # 3
# min
tup = (1, 2, 3)
print(min(tup)) # 1
# sum
tup = (1, 2, 3)
print(sum(tup)) # 6
# tuple concatenation
tup1 = (1, 2, 3)
tup2 = (4, 5)
tup3 = tup1 + tup2
print(tup3) # (1, 2, 3, 4, 5)
# manipulate tuple data by converting it to list
tup = (1, 2, 3)
x = list(tup)
x[1] = 4
tup = tuple(x)
print(tup) # (1, 4, 3)