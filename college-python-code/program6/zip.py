import pathlib
from zipfile import ZipFile
from os.path import isfile, isdir
import sys

directory = input("Enter the directory you want to backup: ")

if (not isdir(directory)):
    print(f"{directory} doesn't exist")
    sys.exit(0)

curDir = pathlib.Path(directory)

with ZipFile("newfile.zip", "w") as archive:
    for file_path in curDir.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curDir))

if (isfile("newfile.zip")):
    print("zip created successfully")
else:
    print("zip was not created")
