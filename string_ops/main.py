def first_last_2_character(param):
    """Takes a string statement and returns 
    the first 2 and last 2 characters"""
    first_2 = param[:2]
    last_2 = param[-2:]
    if len(param) < 2:
        return ""
    return first_2 + last_2

word = input("Input a word or statement: ")
print(first_last_2_character(word))