''' if-else conditional statements '''

# if-else
x = 5
if x > 3:
    print("x is greater than 3")
else:
    print("x is less than or equal to 3")
    
# if-elif-else
x = 5
if x > 3:
    print("x is greater than 3")
elif x == 3:
    print("x is equal to 3")
else:
    print("x is less than 3")
    
# nested if-else
x = 5
if x > 3:
    if x == 5:
        print("x is equal to 5")
    else:
        print("x is greater than 3")
else:
    print("x is less than 3")
    
# shorthand if-else
x = 5
print("x is greater than 3") if x > 3 else print("x is less than or equal to 3")

a = 5
b = 3
print(a) if a > b else print(b) # 5
print(a) if a < b else print(b) # 3