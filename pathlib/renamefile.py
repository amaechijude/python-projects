from pathlib import Path

def rename_file(file_name, new_name, file_extension):
    current_path = Path.cwd()
    num = 1
    for items in current_path.iterdir():
        if items.is_file() and items.suffix == file_extension:
            if items.stem == file_name:
                update_name = new_name + file_extension
                items.rename(update_name)
                print(f"File name is succefully changed from '{file_name+file_extension}' to '{update_name+file_extension}'")
                return
            elif file_name == 'all':
                update_name = new_name + str(num) + file_extension
                items.rename(update_name)
                num += 1
                print(f"File name is succefully changed from '{items.name}' to '{update_name}'")

rename_file('all', 'test', '.txt')