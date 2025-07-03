''' strings '''

# string
x = "Hello World!"

# string length
x = len("Hello World!")

# multi line string
x = """Hello
World!"""

# string concatenation
x = "Hello " + "World!"

# string repetition
x = "Hello" * 3
print(x) # HelloHelloHello

# string slicing
x = "Hello World"
print(x[0]) # H
print(x[1]) # e
print(x[-1]) # d
print(x[-2]) # l
print(x[0:5]) # Hello
print(x[:5]) # Hello
print(x[6:]) # World
print(x[-5:]) # World
print(x[0:5:2]) # Hlo
print(x[-3:-1]) # rl
print(x[::2]) # HloWrd
print(x[::-2]) # drWolH
print(x[::-1]) # dlroW olleH

# string formatting
x = "Hello {}!".format("World") # Hello World!
x = "Hello {0}!".format("World") # Hello World!
x = "Hello {name}!".format(name="World") # Hello World!
x = "Hello {0}! My name is {1}.".format("World", "John") # Hello World! My name is John.
x = "Hello {name}! My name is {name}.".format(name="John") # Hello John! My name is John.
x = "Hello {0}! My name is {0}.".format("John") # Hello John! My name is John.
x = "Hello {0}! My name is {1}.".format("John", " World") # Hello John! My name is World.
x = "Hello {0}! My name is {1}.".format("John", "World") # Hello John! My name is World.

# string methods
# capitalize
x = "hello".capitalize() # Hello
# casefold
x = "HELLO".casefold() # hello
# center
x = "hello".center(10) #   hello
# count
x = "hello".count("l") # 2
# encode
x = "hello".encode() # b'hello'
# endswith
x = "hello".endswith("o") # True
# expandtabs
x = "hello\tworld".expandtabs() # hello   world
# find
x = "hello".find("l") # 2
# to upper case
x = "hello".upper() # HELLO
# to lower case
x = "HELLO".lower() # hello
# to title case
x = "hello world".title() # Hello World
# to swap case
x = "Hello World".swapcase() # hELLO wORLD
# to capitalize
x = "hello world".capitalize() # Hello world
# to casefold
x = "HELLO WORLD".casefold() # hello world
# to center
x = "hello".center(10) #   hello
# to count
x = "hello".count("l") # 2
# r_strip (remove trailing whitespace)
x = " hello ".rstrip() # " hello"
# l_strip (remove leading whitespace)
x = " hello ".lstrip() # "hello "
# strip (remove whitespace)
x = " hello ".strip() # "hello"
# encode
x = "hello".encode() # b'hello'
# endswith
x = "hello".endswith("o") # True
# replace
x = "hello".replace("o", "0") # hell0
# split
x = "hello world".split() # ["hello", "world"]
# join
x = " ".join(["hello", "world"]) # hello world
# startswith
x = "hello".startswith("h") # True
# format
x = "Hello {}!".format("World") # Hello World!
# format_map
x = "Hello {name}!".format_map({"name": "World"}) # Hello World!
# index
x = "hello".index("l") # 2
# isalnum
x = "hello123".isalnum() # True
# isalpha
x = "hello".isalpha() # True
# isascii
x = "hello".isascii() # True
# isdecimal
x = "123".isdecimal() # True
# isdigit
x = "123".isdigit() # True
# isidentifier
x = "hello".isidentifier() # True
# islower
x = "hello".islower() # True
# isnumeric
x = "123".isnumeric() # True
# isprintable
x = "hello".isprintable() # True
# isspace
x = " ".isspace() # True



''' f strings '''

# without f string
message = "Hi, I am {1}, from {0}."
name = "Abdullah"
country = "Pakistan"
print(message.format(country, name)) # Hi, I am Abdullah, from Pakistan.

# with f string
name = "Abdullah"
country = "Pakistan"
print(f"Hi, I am {name}, from {country}.") # Hi, I am Abdullah, from Pakistan.

price = 49.09999
quantity = 3
total = price * quantity
print(f"Total: {total:.2f}") # Total: 147.30

print(f"Sum of 5 and 3 is {5 + 3}") # Sum of 5 and 3 is 8



''' doc strings '''

# doc string
def greet():
    """This function greets the user."""
    print("Hello World!")
print(greet.__doc__) # This function greets the user.

def twosum(a, b):
    '''This function calculates the sum of two numbers.'''
    return a + b
print(twosum.__doc__) # This function calculates the sum of two numbers.

def greet(name):
    print("Hello " + name + "!")
    '''This function greets the user.'''
print(greet.__doc__) # None