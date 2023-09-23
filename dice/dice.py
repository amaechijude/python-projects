import random
roll_again = "Y"
while roll_again == "Y":
    x = random.randint(1,6)
    y = random.randint(1,6)
    print(f"Dice_1 = {x}")
    print(f"Dice_2 = {y}")
    roll_again = input("Do you want to roll the dice again? Y/N: ").upper()
    if roll_again != "Y":
        print("Goodbye")
        quit()
