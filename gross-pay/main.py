print("Welcome to gross pay calculator")
hour = int(input("Input your average work hours per day: "))
rate = float(input("Input your average wage rate per hour: "))
def get_rate(h,r):
    if hour <= 40:
        result = round(float(hour*rate), 2)
        print(f"Your average gross pay per day is ${result}")
    else:
        extra = (hour-40)*rate*1.5
        result = round(float((40*rate)+(extra)), 2)
        print(f"Your average gross pay per day is ${result}")

get_rate(hour,rate)