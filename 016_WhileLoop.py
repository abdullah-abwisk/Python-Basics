''' while loop '''

# while loop
x = 0
while x < 5:
    print(x) # 01234
    x += 1
    
# while loop with break
x = 0
while x < 5:
    if x == 3:
        break
    print(x) # 012
    x += 1
    
# while loop with continue
x = 0
while x < 5:
    if x == 3:
        x += 1
        continue
    print(x) # 0124
    x += 1

# while loop with else
x = 0
while x < 5:
    print(x) # 01234
    x += 1
else:
    print("Loop completed!")
    
# while loop with pass
x = 0
while x < 5:
    pass
print(x) # 5

# do-while loop
secret_word = "python"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7: 
        break