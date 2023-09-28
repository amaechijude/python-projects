from tabulate import tabulate
n = [
    ["names".title(), "language".title(), "proficiency".title()],
    ["Amaechi", "Python", 85], 
    ["Rome", "Golang", 70],
    ["Jude", "Javascript", 60]
    ]
def create_row_func(create_row):
    while create_row.upper() == "Y":
        create_row = input("\nDo you want to add another row? (Y/N): ")
        if create_row.upper() != "Y":
            break
        else:
            name = input("Input the persons name: ")
            lang = input("Input the person's language : ")
            pro = input("Input their profciency level: ")
            print("\n")
            #append the input to a new row
            row = []
            row.append(name)
            row.append(lang)
            row.append(pro)
            #append the new row to the *n list
            n.append(row)
            print(f"{tabulate(n, headers='firstrow')}")
    return "Bye!"