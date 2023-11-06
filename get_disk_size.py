import os
import psutil

def get_disk_size(path):
    total = 0
    path_contents = os.scandir(path)
    for items in path_contents:
        file_size = os.path.getsize(items)
        total += file_size
    return f"Total size is {total} bytes"

path_name = './'
func = get_disk_size(path_name)
print(func)
with open("disk_usage.txt", "w") as f:
    f.write("Disk usage of {}: {}\n".format(path_name, func))
