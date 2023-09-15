print("Welcome to Best Burger Shop")
size = input("Which size are you ordering, mini, normal or large? Reply with M, N or L: ")
cheese = input("Do you want extra cheese? Reply Y for yes or N for no: ")
mush = input("Do you want add mushrooum? Reply Y for yes or N for no: ")

#M  = $5
#N = $8
#L  = $10
#cheese = 1
#mushroom = 1 or 2
#logic

if size == "M":
    if cheese == "Y":
        if mush == "Y":
            cost = 5+1+1
            print(f"The cost of your order is ${cost}")
        elif mush == "N":
            cost = 5+1+0
            print(f"The cost of your order is ${cost}")
    elif cheese == "N":
        if mush == "Y":
            cost = 5+0+1
            print(f"The cost of your order is ${cost}")
        elif mush == "N":
            cost = 5+0+0
            print(f"The cost of your order is ${cost}")
elif size == "N":
    if cheese == "Y":
        if mush == "Y":
            cost = 8+1+1
            print(f"The cost of your order is ${cost}")
        elif mush == "N":
            cost = 8+1+0
            print(f"The cost of your order is ${cost}")
    elif cheese == "N":
        if mush == "Y":
            cost = 8+0+1
            print(f"The cost of your order is ${cost}")
        elif mush == "N":
            cost = 8+0+0
            print(f"The cost of your order is ${cost}")
elif size == "L":
    if cheese == "Y":
        if mush == "Y":
            cost = 10+1+2
            print(f"The cost of your order is ${cost}")
        elif mush == "N":
            cost = 10+1+0
            print(f"The cost of your order is ${cost}")
    elif cheese == "N":
        if mush == "Y":
            cost = 10+0+2
            print(f"The cost of your order is ${cost}")
        elif mush == "N":
            cost = 10+0+0
            print(f"The cost of your order is ${cost}")
