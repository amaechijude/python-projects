import os
from datetime import datetime
from datefunc import datetime_func as df

#current working directory
def current_working_directory():
    '''prints current working directory
    similar to **pwd** in Linux terminal'''
    cwd = os.getcwd()
    print(cwd)
    return cwd

#change current directory
def change_working_directory(directory):
    '''changes working directory
    similar to **cd** in Linux terminal'''
    os.chdir(directory)

def display_directory_entries(directory):
    '''prints all items in current/specified directory
    similar to **ls** in Linux terminal'''
    ls = os.scandir(directory)
    print("{:<23} {:<20} {:<15} {}".format("File Name", "Size",r"File/Folder", "Modification Tme"))
    for i in ls:
        time = os.path.getmtime(i) #modification time
        size = os.path.getsize(i)
        tm = df(time)
        if i.is_dir():
            print("{:<23} {:<20} {:<15} {}".format(i.name, str(size)+" bytes",'folder', tm))
        elif i.is_file():
            print("{:<23} {:<20} {:<15} {}".format(i.name, str(size)+" bytes", "file", tm))

# current_directory = './', upper_one = '../', upper_two = '.../' and so on
d0 = str(current_working_directory())
d1 = './'
d2 = '../'
d3 = '.../'

display_directory_entries(d1)
'''
change_working_directory(d2)
current_working_directory()
change_working_directory(d0)
current_working_directory()'''