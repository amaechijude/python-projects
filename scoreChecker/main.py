import score_func as sc

print("Welcome to score checker")
try:                                                                                        score = int(input("Input your score: "))
except ValueError:
    print("Input a numeric value. 1 try remaining!")
    try:
        score = int(input("Input your score: "))
    except:
        print("Try again")
        quit()

r = sc.scores(score)
print(r)

