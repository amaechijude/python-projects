#side = int(input("Input the value of the lenght: "))
def area_of_square(side):
    area = side*side
    print(f"The area is {area}")

try:
    side = int(input("Input the value of the lenght: "))
except:
    print("Input a numeric value")

side = int(input("Input the value of the lenght: "))
area_of_square(side)
