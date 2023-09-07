def name_func(f_name,l_name):
    result = f_name.title()
    res = l_name.title()
    return f"{result} {res}"
    #print(res)
f_name = input("First name is: ").title()
l_name = input("Last name is: ").title()

output = name_func(f_name,l_name)
#ret_func("amAEchi", "juDE"
def percentage_score(x,y):
    return (x/y)*100
x = int(input("Input your score: "))
y = int(input("Input the total score: "))

output2 = percentage_score(x,y)

print(f"Your name is {output}")
print(f"Your percentage score is {output2}%")
