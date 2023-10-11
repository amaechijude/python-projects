def score_converter(param_dictionary):
    '''Returns students grade
    with respect to their score'''
    result = {}
    for keys in param_dictionary:
        if param_dictionary[keys] < 40:
            result[keys] = "Failed"
        if param_dictionary[keys] >= 40:
            result[keys] = "You got D"
        if param_dictionary[keys] >= 50:
            result[keys] = "You got C"
        if param_dictionary[keys] >= 60:
            result[keys] = "You got B"
        if param_dictionary[keys] >= 70:
            result[keys] = "You got A"

    return result

student_score = {
    "John": 90,
    "Jane": 65,
    "April": 51,
    "Anna": 48,
    "Harriet": 39
}

print(score_converter(student_score))