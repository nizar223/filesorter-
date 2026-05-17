from pathlib import Path
import shutil
from config import EXTENSIONS

# filemanager by noozer

path = Path("your path")

folders = {}


# folder creation

for folder in EXTENSIONS.keys():
    folder_path = path / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    folders[folder] = folder_path

# sortation

for file in path.iterdir():
    if file.is_file():
        for category, extensions in EXTENSIONS.items():
            suffix = file.suffix.lower().strip()
            if suffix in extensions:
                target =  folders[category] / file.name
                shutil.move(str(file), str(target))

                print(f"Moved {file} to {category}")
                break


