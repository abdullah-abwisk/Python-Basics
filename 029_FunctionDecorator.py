''' Decorators '''

# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
# A decorator is a small function that takes another function as an argument and extends the behavior of the
# latter function without explicitly modifying it.

# Decorators are usually called before the definition of a function you want to decorate.
# They are used to add a new functionality to an existing object without modifying its structure.
# Decorators are a form of metaprogramming and are used to modify the behavior of function or methods.


# Example 1: Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator # This is a decorator
def say_hello():
    print("Hello!")
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


# Example 2: Decorator with arguments
def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator2 # This is a decorator
def add(a, b):
    print(a + b)

my_decorator2(add)(1, 2)
# Output:
# Something is happening before the function is called.
# 3
# Something is happening after the function is called.

