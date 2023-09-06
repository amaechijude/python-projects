print("Welcome to score checker")
try:
    score = float(input("Input your score: "))
except:
    print("Input a numeric value")

score = float(input("Input your score: "))

if score >= 0 and score < 40:
    print(f"Your score is {score} and your grade is F")
elif score >= 40 and score < 45:
    print(f"Your score is {score} and your grade is E")
elif score >= 45 and score < 50:
    print(f"Your score is {score} and your grade is D")
elif score >= 50 and score < 60:
    print(f"Your score is {score} and your grade is C")
elif score >= 60 and score < 70:
    print(f"Your score is {score} and your grade is B")
elif score >= 70 and score <= 100:
    print(f"Your score is {score} and your grade is A")
else:
    print("Your score is out of range")
