def scores(score):
    if score < 40:
        output = f"Your score is {score} and your grade is F"
        return output
    elif score < 45:
        output = f"Your score is {score} and your grade is E"
        return output
    elif score < 50:
        output = f"Your score is {score} and your grade is D"
        return output
    elif score < 60:
        output = f"Your score is {score} and your grade is C"
        return output
    elif score < 70:
        output = f"Your score is {score} and your grade is A"
        return output
    elif score <= 100:
        output = f"Your score is {score} and your grade is A"
        return output
    else:
        output = "Your score is out of range"
        return output
    return output
