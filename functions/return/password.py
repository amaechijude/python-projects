def password_checker(x):
    if len(x) < 8:
        return "False, password lenght less than 8 characters"
    else:
        return "True, password lenght greater than 8 characters"

#p = password_checker(x)
x = input("Input a password: ")

print(password_checker(x))
