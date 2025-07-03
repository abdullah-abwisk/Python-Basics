''' match case '''

# match case
x = 5
match x:
    case 3:
        print("x is equal to 3")
    case 5:
        print("x is equal to 5")
    case _ if x < 0:
        print("x is less than 0")
    case _:
        print("x is not equal to 3 or 5")