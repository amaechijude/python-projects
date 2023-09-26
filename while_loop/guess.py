import random,math
x = int(input("Enter lower bound: "))
y = int(input("Enter upper bound: "))
c = int(math.log(y-x+1,2))
print(f"\n\tYou only have {c} chances left\n")
r = random.randint(x,y)
count = 0
while count < c:
    count += 1
    g = int(input("Guess a Number: "))
    if g == r:
        print(f"Congratulations. The number is {r} and you did it in {i+1} try")
        break
    if g < x or g > y:
        print(f"{g} is out of bounds")
        #g = int(input("Guess a Number: "))
    if g > r:
        print(f"You guessed too high\n")
        #g = int(input("Guess a Number: "))
    if g < r:
        print(f"You guessed too low\n")
        #g = int(input("Guess a Number: "))
    
print(f"\nThe number is {r}. \n\tBetter luck next time")

"""
if i == 3:
        print(f"The number is {r}.")
        print(f"Better luck next time:")
        break
"""
