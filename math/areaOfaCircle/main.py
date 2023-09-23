import math
print("Welcome to area of circle Calculator")
r = float(input("Input the radius of the circle: "))
p = math.pi
a = math.pow(r,2)
area = round(p*a, 2)
#area = round(p*(r**2), 2)
print(f"The area of the circle is {area}")
