def read_lines(file_name, line_num):
    '''The **readlines() function of open files
    returns a list with each line as elements.
    Hence index can be used to target a single line
    The file name/path must be enclosed in a quote'''
    param_line = int(line_num) - 1
    with open(file_name, mode='r') as file:
        lines = file.readlines()
        if param_line < len(lines):
            return f"Text on line {line_num} is: {lines[param_line]}"
        else:
            return f'Line {line_num} does not exist in {file_name}'

def read_single_line(file_na):
    with open(file_na, mode='r') as f:
        li = f.readline()
        while li != "":
            print(li, end="")
            li = f.readline()

output = read_lines("text_file.txt", 4)
print(f"Readline output {output}\n")
read_single_line('text_file.txt')