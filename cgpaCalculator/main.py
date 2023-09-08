import cgpa as cg
print("Welcome to CGPA grading portal")
try:
    #cgpa <= 5
    cgpa = float(input("Input your CGPA: "))
except:
    print("Input a numerical and valid CGPA")
    cgpa = float(input("Input your CGPA: "))

#Calling the cgpa function
result = cg.calc(cgpa)
print(result)
