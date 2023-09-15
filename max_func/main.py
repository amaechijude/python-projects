student_score = [23, 45, 78, 94, 33, 45, 28, 43]
high_score = 0
for score in student_score:
    if score > high_score:
        high_score = score
        print(score, high_score)
#r = max(student_score)
#print(f"The highest score is: {r}")
