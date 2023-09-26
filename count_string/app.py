def count_string(word, letter):
    w = word.upper()
    l = letter.upper()
    num_of_letter = 0
    for char in w:
        if char.upper() == l:
            num_of_letter += 1
    return f"{letter} appears {num_of_letter} times in {word}"

x = input("Input a word or statement: ")
y = input("Input an alphabet you want to count in the above: ")
print(count_string(x,y))