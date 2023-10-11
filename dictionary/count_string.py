def count_string(word):
    result = {}
    for char in word:
        if char not in result:
            result[char] = 1
        else:
            result[char] = result[char] + 1
    return result

user = input("Input a word: ")
print(count_string(user))