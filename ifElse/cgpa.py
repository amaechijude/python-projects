print("Welcome to CGPA grading portal")
try:
    #cgpa <= 5
    cgpa = float(input("Input your CGPA: "))
except:
    print("Input a numerical and valid CGPA")

cgpa = float(input("Input your CGPA: "))
if cgpa<=5.00 and cgpa>=4.50:
    print("You have first class honours")
elif cgpa<4.50 and cgpa>= 3.5:
    print("You have second class upper")
elif cgpa<3.5 and cgpa>=2.5:
    print("You have second class lower")
elif cgpa<2.5 and cgpa>=1.5:
    print("You have third class")
elif cgpa<1.5:
    print("You have failed")
else:
    print("Your cgpa is out of bounds")
