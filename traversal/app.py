name = input("Input name: ")
index = -1
length = -1 * len(name)
while index >= length:
    letter = name[index]
    index -= 1
    print(letter)
