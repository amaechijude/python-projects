print("Welcome to gross pay calculator")
hour = int(input("Input your average work hours per day: "))
rate = float(input("Input your average wage rate per hour: "))
result = round(float(hour*rate), 2)
#result = format(float(hour*rate), '.2f')
print("Your average gross pay per day is","$"+str(result))