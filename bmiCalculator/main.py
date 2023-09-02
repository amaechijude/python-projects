print("Welcome to Body Mass Index Calculator")
mass = float(input("Input your weigth (in kg): "))
height = float(input("Input your height (in m): "))
bmi = round(float((mass)/height**2), 2)

if bmi<18.5:
    print(f"Your body mass index is {bmi} and you are underweight")
elif bmi>=18.5 and bmi<25:
    print(f"Your body mass index is {bmi} and you have normal weight")
elif bmi>=25 and bmi<30:
    print(f"Your body mass index is {bmi} and you are overweight")
elif bmi>=30 and bmi<35:
    print(f"Your body mass index is {bmi} and you are class 1 obese")
elif bmi>=30 and bmi<35:
    print(f"Your body mass index is {bmi} and you are class 1 obese")
elif bmi>=35 and bmi<40:
    print(f"Your body mass index is {bmi} and you are class 2 obese")
elif bmi>40:
    print(f"Your body mass index is {bmi} and you are extreme obese")
