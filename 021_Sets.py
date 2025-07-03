''' sets '''

# set
# set does not allow duplicate values
x = {1, 2, 3, 4, 5}
print(1 in x) # True
print(6 in x) # False
x = {1, 2, 3, 4, 5, 5, 2, 1, 4}
print(x) # {1, 2, 3, 4, 5}
for i in x:
    print(i, end=", ") # 1, 2, 3, 4, 5,
print(x[1]) # TypeError: 'set' object is not subscriptable
x = {1, 2, 3, 4, 5}
print(type(x)) # <class 'set'>
x = {}
print(type(x)) # <class 'dict'>

# set methods
# union
x = {1, 2, 3}
y = {4, 5}
z = x.union(y)
print(z) # {1, 2, 3, 4, 5}
# intersection
x = {1, 2, 3}
y = {2, 3, 4}
z = x.intersection(y)
print(z) # {2, 3}
# union update
x = {1, 2, 3}
y = {4, 5}
x.update(y)
print(x) # {1, 2, 3, 4, 5}
# intersection update
x = {1, 2, 3}
y = {2, 3, 4}
x.intersection_update(y)
print(x) # {2, 3}
# difference
x = {1, 2, 3}
y = {2, 3, 4}
z = x.difference(y)
print(z) # {1}
# difference update
x = {1, 2, 3}
y = {2, 3, 4}
x.difference_update(y)
print(x) # {1}
# symmetric difference
x = {1, 2, 3}
y = {2, 3, 4}
z = x.symmetric_difference(y)
print(z) # {1, 4}
# symmetric difference update
x = {1, 2, 3}
y = {2, 3, 4}
x.symmetric_difference_update(y)
print(x) # {1, 4}
# add
x = {1, 2, 3}
x.add(4)
print(x) # {1, 2, 3, 4}
# remove
x = {1, 2, 3}
x.remove(2)
print(x) # {1, 3}
# discard
x = {1, 2, 3}
x.discard(2)
print(x) # {1, 3}
# pop
x = {1, 2, 3}
x.pop()
print(x) # {2, 3}
# clear
x = {1, 2, 3}
x.clear()
print(x) # set()
# copy
x = {1, 2, 3}
y = x.copy()
print(y) # {1, 2, 3}
# isdisjoint
x = {1, 2, 3}
y = {4, 5}
print(x.isdisjoint(y)) # True
# issubset
x = {1, 2, 3}
y = {1, 2}
print(y.issubset(x)) # True
# issuperset
x = {1, 2, 3}
y = {1, 2}
print(x.issuperset(y)) # True
# len
x = {1, 2, 3}
print(len(x)) # 3
# delete set
x = {1, 2, 3}
del x
# print(x) # NameError: name 'x' is not defined