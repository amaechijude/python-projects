def calc(cgpa):
    if cgpa<=5.00 and cgpa>=4.50:
        output = "You have first class honours"
        return output
    elif cgpa<4.50 and cgpa>= 3.5:
        output = "You have second class upper"
        return output
    elif cgpa<3.5 and cgpa>=2.5:
        output = "You have second class lower"
        return output
    elif cgpa<2.5 and cgpa>=1.5:
        output = "You have third class"
        return output
    elif cgpa<1.5:
        output = "You have failed"
        return output
    else:
        output = "Your cgpa is out of bounds"
        return output
    return output
