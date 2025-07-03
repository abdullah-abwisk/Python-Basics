''' recursion '''

# factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # 120

# fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5)) # 5
print(fibonacci(10)) # 34
print(fibonacci(20)) # 4181