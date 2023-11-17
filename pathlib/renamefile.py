from pathlib import Path

def rename_file(file_name, new_name, file_type):
    current_path = Path.cwd()
    for items in current_path.iterdir():
        if items.is_file() and items.suffix == file_type:
            if items.stem == file_name:
                update_name = new_name + file_type
                items.rename(update_name)
                print(f"File name is succefully changed from '{file_name+file_type}' to '{update_name+file_type}'")

rename_file('text1', 'file1', '.txt')