number = 0
num = []
while number < 10:
    number += 1
    if number == 5:
        continue
    num.append(number)
    print(number, num)
