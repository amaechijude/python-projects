import os

'''os.walk recursively returns all contents in a current directory  as well as the contents of its subdirectories.
    It has "topdown" aproach in which it starts from the root folder \
        to the last subfolder and "bottom-up" in reverse'''

def top_down_walk():
    '''Starts from the root directory
        down to the deepest directory'''
    for dirpath, dirnames, filenames in os.walk("../"):
        if "git" in str(dirpath):
            continue
        else:
            print(f"Directory: {dirpath}")
            print("----includes these directorries----")
            for dirname in dirnames:
                print(dirname)
            print("----includes these files----")
            for files in filenames:
                print(f"{files}")
            print()

def bottom_up_walk():
    '''Starts from the deepest subdirectory
        up to the root directory'''
    for dirpath, dirnames, filenames in os.walk("../", topdown=False):
        if "git" in str(dirpath):
            continue
        print("Directory path: ", dirpath)
        print("----includes these directorries----")
        for dirname in dirnames:
            print(dirname)
        print("----includes these files----")
        for files in filenames:
            print(f"{files}")
        print()

top_down_walk()
#bottom_up_walk()