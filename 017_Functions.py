''' functions '''

# function
def greet():
    print("Hello World!")
greet() # Hello World!

# function with parameters
def greet(name):
    print("Hello " + name + "!")
greet("John") # Hello John!

# function with return value
def greet(name):
    return "Hello " + name + "!"
message = greet("John")
print(message) # Hello John!

# function to calculate sum
def add(x, y):
    return x + y
result = add(5, 3)
print(result) # 8

# function with default parameter
def greet(name="World"):
    print("Hello " + name + "!")
greet() # Hello World!
greet("John") # Hello John!

# function with 2 default parameters
def sum (x=5, y=3):
    return x + y
result = sum()
print(result) # 8
result = sum(7)
print(result) # 10
result = sum(7, 4)
print(result) # 11

# function with keyword arguments
def greet(name, message):
    print("Hello " + name + "! " + message)
greet(message="Good Morning!", name="John") # Hello John! Good Morning!
greet(name="John", message="Good Morning!") # Hello John! Good Morning!
greet("John", "Good Morning!") # Hello John! Good Morning!
# greet(name="John", "Good Morning!") # Error
greet("John", message="Good Morning!") # Error

# function with variable length arguments
def greet(*names):
    for name in names:
        print("Hello " + name + "!")
greet("John", "Jane", "Jack") # Hello John! Hello Jane! Hello Jack!
greet("John") # Hello John!
greet() # No output
greet("John", "Jane", "Jack", "Jill") # Hello John! Hello Jane! Hello Jack! Hello Jill!
greet("John", "Jane") # Hello John! Hello Jane!

# function with variable length keyword arguments
def greet(**names):
    for name, message in names.items():
        print("Hello " + name + "! " + message)
greet(John="Good Morning!", Jane="Good Afternoon!") # Hello John! Good Morning! Hello Jane! Good Afternoon!
greet(John="Good Morning!") # Hello John! Good Morning!
greet() # No output

# function with variable length arguments and keyword arguments
def greet(*names, **messages):
    for name in names:
        for message in messages.values():
            print("Hello " + name + "! " + message)
greet("John", "Jane", John="Good Morning!", Jane="Good Afternoon!") # Hello John! Good Morning! Hello Jane! Good Afternoon!
greet("John", John="Good Morning!") # Hello John! Good Morning!
greet() # No output

# function with dictionary input
def greet(*names):
    print("Hello", name["fname"], name["lname"])
name = {"fname": "John", "lname": "Doe"}
greet(name) # Hello John Doe



''' lambda functions '''

# lambda function
x = lambda a : a + 10
print(x(5)) # 15
x = lambda a, b : a + b
print(x(5, 3)) # 8
x = lambda a, b, c : a + b + c
print(x(5, 3, 2)) # 10
x = lambda a, b, c, d : a + b + c + d
print(x(5, 3, 2, 1)) # 11
cube = lambda x: x ** 3
print(cube(3)) # 27

def cube(fx, n):
    return fx(n)

result = cube(lambda x: x ** 3, 3)