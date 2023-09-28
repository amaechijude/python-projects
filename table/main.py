from tabulate import tabulate
n = [
    ["names".title(), "language".title(), "proficiency(&)".title()],
    ["Amaechi", "Python", "85%"], 
    ["Rome", "Golang", "70%"],
    ["Jude", "Javascript", "60%"]
    ]
print(len(n))
def create_row_func():
    create_row = "Y"
    while create_row.upper() == "Y":
        create_row = input("\nDo you want to add another row? (Y/N): ")
        if create_row.upper() != "Y":
            break
        else:
            name = input("Input the persons name: ").title()
            lang = input("Input the person's language : ")
            pro = input("Input their profciency level (in %): ")+"%"
            print("\n")
            #append the input to a new row
            row = []
            row.append(name)
            row.append(lang)
            row.append(pro)
            #append the new row to the *n list
            n.append(row)
            print(f"{tabulate(n, headers='firstrow')}")
    return len(n)

def create_column_func():
    create_column = "Y"
    while create_column.upper() == "Y":
        create_column = input("\nDo you want to add another column? (Y/N): ")
        if create_column.upper() != "Y":
            break
        else:
            for index in range(0,len(n)):
                if index == len(n):
                    break
                else:
                    n0 = index
                print(index)
            '''
                heading = input("Input the heading of the row: ")
                n_0 = index
                n_1 = index
                n_2 = index
                n_3 = index
                n_4 = index
                row_1 = input(f"Input the {n[n_1][0]}'s {heading} : ")
                row_2 = input(f"Input the {n[n_2][0]}'s {heading} : ")
                row_3 = input(f"Input the {n[n_3][0]}'s {heading} : ")
                row_4 = input(f"Input the {n[n_4][0]}'s {heading} : ")
                n[n_0].append(heading)
                n[n_1].append(row_1)
                n[n_2].append(row_2)
                n[n_3].append(row_3)
                n[n_4].append(row_4)
            print(f"{tabulate(n, headers='firstrow')}")'''
    return "Bye!"

#calling the function
print(tabulate(n, headers='firstrow'))
print(create_row_func())
print(create_column_func())