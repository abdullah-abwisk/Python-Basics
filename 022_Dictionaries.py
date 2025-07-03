''' dictionaries '''

# dictionary
# dictionary is a collection of key-value pairs
x = {"name": "John", "age": 36}
print(x["name"]) # John
print(x["age"]) # 36
print(x.get("name")) # John
print(x.get("age")) # 36

# dictionary methods
x = {"name": "John", "age": 36}
print(x) # {'name': 'John', 'age': 36}
# keys
print(x.keys()) # dict_keys(['name', 'age'])
# iterate keys
for key in x.keys():
    print(key, end=", ") # name, age,
    print(x[key]) # John, 36
# iterate keys and values
for key, value in x.items():
    print(key, value) # name John, age 36
# values
print(x.values()) # dict_values(['John', 36])
# items
print(x.items()) # dict_items([('name', 'John'), ('age', 36)])
# update
x.update({"name": "Jane"})
print(x) # {'name': 'Jane', 'age': 36}
y = {"city": "New York"}
x.update(y)
print(x) # {'name': 'Jane', 'age': 36, 'city': 'New York'}
# pop
x.pop("name")
print(x) # {'age': 36, 'city': 'New York'}
# popitem
x.popitem()
print(x) # {'age': 36}
# clear
x.clear()
print(x) # {}
# copy
x = {"name": "John", "age": 36}
y = x.copy()
print(y) # {'name': 'John', 'age': 36}
# fromkeys
x = dict.fromkeys(["name", "age", "city"], "Unknown")
print(x) # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
# setdefault
x = {"name": "John", "age": 36}
x.setdefault("city", "New York")
print(x) # {'name': 'John', 'age': 36, 'city': 'New York'}
# get
x = {"name": "John", "age": 36}
print(x.get("name")) # John
# len
x = {"name": "John", "age": 36}
print(len(x)) # 2
# delete dictionary
x = {"name": "John", "age": 36}
del x
# print(x) # NameError: name 'x' is not defined