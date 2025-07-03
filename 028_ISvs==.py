''' is vs == '''

# is vs ==
# is : reference equality
# == : value equality

a = 4
b = 4

print(a is b) # True (checks if a and b refer to the same object)
print(a == b) # True (checks if a and b have the same value)

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # False (checks if a and b refer to the same object)
print(a == b) # True (checks if a and b have the same value)

a = [1, 2, 3]
b = a

print(a is b) # True (checks if a and b refer to the same object)
print(a == b) # True (checks if a and b have the same value)

a = [1, 2, 3]
b = a[:]

print(a is b) # False (checks if a and b refer to the same object)
print(a == b) # True (checks if a and b have the same value)

a = None
b = None

print(a is b) # True (checks if a and b refer to the same object)
print(a == b) # True (checks if a and b have the same value)
print(a is None) # True (checks if a is None)