from pathlib import Path

path_test = Path.cwd() /"archive"/"test.txt"
#print the test.txt filename
print(f"The file name is{path_test.name}")
#Prints parent directory
print(path_test.parent)
#Prints parent directory of the above
print(path_test.parent.parent)