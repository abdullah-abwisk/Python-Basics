''' for loop '''

# for loop
name = "Abdullah"
for letter in name:
    print(letter, end=", ") # A, b, d, u, l, l, a, h,
    
# for loop with range
for i in range(5):
    print(i, end=", ") # 0, 1, 2, 3, 4,
    
# for loop with range and step
for i in range(0, 5, 2):
    print(i, end=", ") # 0, 2, 4,
    
# for loop with range and negative step
for i in range(5, 0, -1):
    print(i, end=", ") # 5, 4, 3, 2, 1,
    
# for loop with limited range
for i in range(2, 5):
    print(name[i]) # dul
    
# for loop with length
name = "Abdullah"
for i in range(len(name)):
    print(name[i], end=", ") # A, b, d, u, l, l, a, h,
    
# for loop with enumerate
name = "Abdullah"
for i, letter in enumerate(name):
    print(i, letter, end=", ") # 0 A, 1 b, 2 d, 3 u, 4 l, 5 l, 6 a, 7 h,
    
# for loop with break
name = "Abdullah"
for letter in name:
    if letter == "l":
        break
    print(letter, end=", ") # A, b, d, u,
    
# for loop with continue
name = "Abdullah"
for letter in name:
    if letter == "l":
        continue
    print(letter, end=", ") # A, b, d, u, a, h,
    
# for loop with else
name = "Abdullah"
for letter in name:
    print(letter, end=", ") # A, b, d, u, l, l, a, h,
else:
    print("Loop completed!")
    
for i in []:
    print(i)
else:
    print("Loop completed!") # Loop completed!
    
# for loop with pass
name = "Abdullah"
for letter in name:
    pass
print(letter) # NameError: name 'letter' is not defined

# for loop on list
names = ["John", "Jane", "Jack"]
for name in names:
    print(name, end=", ") # John, Jane, Jack,