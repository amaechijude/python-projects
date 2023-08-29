print("Welcome to the #100DaysOfCode Challenge")
totalDays = 100
name = input("Input your name\n")
language = input("Input your preffered language\n")
days = input("How many days have you elapsed?\n")
daysElapsed = int(days)
length = len(name)
print("Your name is ", name, " and the character length of your name is ", length, ".")
print("Also your preffered programming language is ", language)
print("Congratulations for joining the challenge.")
daysRemaining = totalDays-daysElapsed
print("You've spent ", daysElapsed, " days; and have ", daysRemaining, " remaining for you to complete the challenge")
