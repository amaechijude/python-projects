student_scores = [80, 60, 50, 65, 75, 55]

def sum_above_average(scores):
    average_score = (sum(student_scores)) / (len(student_scores))
    sum_above_average = 0
    for score in scores:
        if score > average_score:
            sum_above_average += score
    return sum_above_average

result = sum_above_average(student_scores)
print(result)
