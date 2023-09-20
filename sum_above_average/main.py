student_scores = [80, 60, 50, 65, 75, 55] 
def sum_above_average(param_student_scores):

    sum_of_scores = 0
    no_of_students = 0
    sum_of_average = 0

    for score in param_student_scores:
        sum_of_scores += score
        no_of_students += 1
    average_score = sum_of_scores / no_of_students
    print(average_score, sum_of_scores, no_of_students)

    for score in param_student_scores:
        if score > average_score:
            print(score)
            sum_of_average += score
    return sum_of_average

result = sum_above_average(student_scores)
print(result)
