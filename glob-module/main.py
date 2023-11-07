from glob import glob, iglob
''' glob module returns file names \
    matching specified pattern as a list
'''
# iglob returns the path. it is iterative

def display_png():
    png_files = glob("*.png")
    print(png_files)

def display_file():
    files = glob("*le*")
    print(files)

def display_subdir():
    subdir = iglob("**/*sub*", recursive=True)
    for items in subdir:
        print(items)

display_png()
display_file()
display_subdir()