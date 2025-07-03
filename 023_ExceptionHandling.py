''' exception handling '''

# exception handling
try:
    print(x)
except:
    print("An exception occurred")
    
i = 4
j = 'Abdullah'

try:
    for k in range(10):
        print(int(j) * (k + 1))
except Exception as e:
    print("An exception occurred")
    print(e)
    
try:
    x = int(input("Enter a number: "))
    y = [10, 20, 30]
    y[0] = x
    print(y[x])   
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index out of range")

# finally
try:
    print(x)
except:
    print("An exception occurred")
finally:
    print("The 'try except' is finished") # always executed
    
# raise exception
x = int(input("Enter a number between 1 and 10: "))

if x < 1 or x > 10:
    raise Exception("Number out of range")
else:
    print("Number is in range")
    
# raise exception for index out of range
x = [1, 2, 3, 4, 5]
indx = int(input("Enter an index: "))
if indx < 0 or indx >= len(x):
    raise IndexError("Index out of range")
else:
    print(x[indx])
    
# custom exception
class MyException:
    def __init__(self, message):
        self.message = message
        def __str__(self):
            return self.message
        try:
            x = int(input("Enter a number between 1 and 10: "))
            if x < 1 or x > 10:
                raise MyException("Number out of range")
            else:
                print("Number is in range")
        except MyException as e:
            print(e)
            
# assert
x = 5
assert x > 3
print("Assertion passed")
assert x < 3
print("Assertion failed")