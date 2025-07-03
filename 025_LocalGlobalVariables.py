''' local vs global variables '''

# local and global variables
x = 10 # global variable

def outer():
    x = 20 # local variable
    print(x) # 20
    
print(x) # 10
outer()
print(x) # 10

# calling a local variable outside the function
def functi():
    x = 10 # local variable

print(x) # NameError: name 'x' is not defined
    
# calling a global variable inside a function
x = 10
def funct():
    print(x) # 10
    
funct()

# changing a global variable inside a function
x = 10
def funct():
    global x # declare x as global
    x = 20 # change the value of x
    print(x) # 20
    
funct()
print(x) # 20