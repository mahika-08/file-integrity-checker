from pathlib import Path

def scan_directory(folder_path):
    folder=Path(folder_path)
    files_list=[]
    for item in folder.rglob("*"):
        if item.is_file():
            files_list.append(str(item))
    return files_list