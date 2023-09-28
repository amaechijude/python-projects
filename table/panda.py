import panda as pd

n = [
    ["Amaechi", "Python", 85], 
    ["Jude", "Golang", 70],
    ]

output = pd.DataFrame(n, columns =["names".title(), "programming language".title(), "proficiency level".title()])
print(f"\n{output}")