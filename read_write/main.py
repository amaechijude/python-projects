'''file = open('text_file.txt')
content = file.read()
print(content)
file.close()'''

with open('text_file.txt', mode='r') as file:
    content = file.read()
    print(content)