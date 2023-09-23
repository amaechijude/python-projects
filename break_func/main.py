list_1 =[12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]

def divisible_by_five(x_lists):
    for item in x_lists:
        if item > 130:
            break
        if item % 5 == 0:
            print(item)
    print("STOP")

divisible_by_five(list_1)
