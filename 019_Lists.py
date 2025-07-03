''' lists '''

# list
x = [1, 2, 3, 4, 5]
print(x[0]) # 1
print(x[1]) # 2
print(x[-1]) # 5

# list length
x = [1, 2, 3, 4, 5]
print(len(x)) # 5

# list slicing
x = [1, 2, 3, 4, 5]
print(x[0:3]) # [1, 2, 3]
print(x[:3]) # [1, 2, 3]
print(x[2:]) # [3, 4, 5]
print(x[-3:]) # [3, 4, 5]

# list methods
# append
x = [1, 2, 3]
x.append(4)
print(x) # [1, 2, 3, 4]
# clear
x = [1, 2, 3]
x.clear()
print(x) # []
# copy
x = [1, 2, 3]
y = x.copy()
print(y) # [1, 2, 3]
# count
x = [1, 2, 3, 2, 1]
print(x.count(2)) # 2
# extend
x = [1, 2, 3]
y = [4, 5]
x.extend(y)
print(x) # [1, 2, 3, 4, 5]
# index
x = [1, 2, 3]
print(x.index(2)) # 1
# insert
x = [1, 2, 3]
x.insert(1, 4)
print(x) # [1, 4, 2, 3]
# pop
x = [1, 2, 3]
x.pop()
print(x) # [1, 2]
# remove
x = [1, 2, 3]
x.remove(2)
print(x) # [1, 3]
# reverse
x = [1, 2, 3]
x.reverse()
print(x) # [3, 2, 1]
# sort
x = [3, 1, 2]
x.sort()
print(x) # [1, 2, 3]
# sort reverse
x = [3, 1, 2]
x.sort(reverse=True)
print(x) # [3, 2, 1]
# change item
x = [1, 2, 3]
x[1] = 4
print(x) # [1, 4, 3]
# merge lists
x = [1, 2, 3]
y = [4, 5]
z = x + y
print(z) # [1, 2, 3, 4, 5]
# repeat list
x = [1, 2, 3]
y = x * 3
print(y) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# if item exists
x = [1, 2, 3]
if 2 in x:
    print("Yes")
else:
    print("No")
# if item not exists
x = [1, 2, 3]
if 4 not in x:
    print("Yes")
else:
    print("No")
    
# list comprehension
x = [i for i in range(5)]
print(x) # [0, 1, 2, 3, 4]
x = [i for i in range(5) if i > 2]
print(x) # [3, 4]
x = [i * 2 for i in range(5)]
print(x) # [0, 2, 4, 6, 8]
x = [i for i in range(5) if i % 2 == 0]
print(x) # [0, 2, 4]
x = [i for i in range(5) if i % 2 != 0]
print(x) # [1, 3]
x = ["Ali", "Ahmed", "Abdullah", "John", "Amy"]
y = [i for i in x if "A" in i]
print(y) # ['Ali', 'Ahmed', 'Abdullah', 'Amy']
y = [i for i in x if len(i) > 3]
print(y) # ['Ahmed', 'Abdullah', 'John']
y = [i.upper() for i in x]
print(y) # ['ALI', 'AHMED', 'ABDULLAH', 'JOHN', 'AMY']