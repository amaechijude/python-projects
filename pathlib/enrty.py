from pathlib import Path
def display_directory_entries():
    entries = Path.cwd()
    for entry in entries.iterdir():
        #print the entry names of the current directory
        print(f"File/folder: {entry.name}")
        #filename without suffix
        print(f"Names without extention {entry.stem}")
        #filename with only suffix
        print(f"{entry.suffix}")


display_directory_entries()