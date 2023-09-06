print("Welcome to Love calculator")
name1 = input("Input first lover's name: ").lower()
name2 = input("Input second lover's name: ").lower()

name = name1 + name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = str(t+r+u+e)

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = str(l+o+v+e)

output = true+love
score = int(output)
print(output)

if score < 10 or score > 85:
    print(f"Your love score is {score} and you aren't eligible")
elif score >= 40 and score <= 85:
    print(f"Your love score is {score} and you are qualified for love")
else:
    print(f"Your love score is {score} and you are off-limits")
