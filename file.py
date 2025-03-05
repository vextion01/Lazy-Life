import os
import shutil

## Waring!!! Test this python file first before use it##

def checkPath(dir):
    if not os.path.exists(dir):
        print("The directory does not exist.")
        return
    for file in os.listdir(dir):
        if file == os.path.basename(__file__):  
            continue
        ext = os.path.splitext(file)[1][1:] 
        if ext:  
            folder = os.path.join(dir, ext)
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(dir, file)
            shutil.move(file_path, os.path.join(folder, file))
            print(f"Moved {file} to {ext}")

if __name__ == "__main__":
    pathFolder = input("Enter the folder path: ")
    checkPath(pathFolder)
