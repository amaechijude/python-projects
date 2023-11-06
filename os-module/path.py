import os
abs_path = os.path.abspath('main.py')
print(f"The absolute path is: {abs_path}")

print(os.path.join('folder1', 'folder2', 'logo.png'))
directory_name = os.path.dirname("/data/data/com.termux/files/home/python-projects/os-module/main.py")
base_name = os.path.basename("/data/data/com.termux/files/home/python-projects/os-module/main.py")

print(directory_name)
print(base_name)
