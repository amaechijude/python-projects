print("Welcome to score checker")
try:
    score = float(input("Input your score: "))
except ValueError:
    print("Input a numeric value. 1 try remaining!")
try:
    score = float(input("Input your score: "))
except:
    print("Try again")
    quit()

if score < 40:
    print(f"Your score is {score} and your grade is F")
elif score < 45:
    print(f"Your score is {score} and your grade is E")
elif score < 50:
    print(f"Your score is {score} and your grade is D")
elif score < 60:
    print(f"Your score is {score} and your grade is C")
elif score < 70:
    print(f"Your score is {score} and your grade is B")
elif score <= 100:
    print(f"Your score is {score} and your grade is A")
else:
    print("Your score is out of range")
