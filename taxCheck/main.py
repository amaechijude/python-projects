print("Welcome to tax rate Calculator\n")
income = int(input("Input your gross income: $"))
biz = str(input("Are you a startup? Reply Y for yes or N for no: "))
#taxRate = 0

#logic

if biz == "N" or biz == "n":
    if income <= 11_000:
        taxRate = 10
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax")
    elif income <= 44_725:
        taxRate = 12
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax")
    elif income <= 95_375:
        taxRate = 22
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax fees")
    elif income <= 182_100:
        taxRate = 24
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax fees")
    elif income <= 231_250:
        taxRate = 32
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax fees")
    elif income <= 578_125:
        taxRate = 35
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax fees")
    elif income > 578_125:
        taxRate = 37
        tax = round(float((taxRate/100)*income), 2)
        print(f"Your income is ${income} and your tax rate is {taxRate}%, you should pay ${tax} in tax fees")
elif biz == "Y" or biz == "y":
    print("You are eligible for tax exemption")
