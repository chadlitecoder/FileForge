from pathlib import Path
import shutil 
import json
from collections import Counter
#taking in target and destination folders
print("\n LEAVE EMPTY IF DEFAULT PATHS ARE TO BE USED \n")

rawpath=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Backup")
fp=input("Enter the directory to sort: ")
files_path=Path(fp)
dp=input("Enter the destination for sorted files: ")
destination=Path(dp)
if not fp:
    files_path=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Raw")
if not dp:
    destination=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Data")

#loading dictionaries that tell which extension refers to which type of file
dict_path=Path('C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/file_dict.json')
filetype=dict()
with open(dict_path,'r') as file:
        filetype=json.load(file)

#Copy or Move
def transporter():
    copymove=input("Copy or move?: ")
    #Move sorted source to target
    if copymove.lower().strip()=="move":
        for filename in files_path.iterdir():
            if str(filename.suffix) in filetype:
                Path(destination/ filetype[str(filename.suffix)]).mkdir(parents=True, exist_ok=True)
                shutil.copy(files_path/ str(filename.name), destination/ filetype[str(filename.suffix)])
                shutil.copy(files_path/ str(filename.name), rawpath)
            else:
                typeinput=input(f"What is the type of file called with '{str(filename.suffix)}' extension ?")
                filetype[str(filename.suffix)]=typeinput
                Path(destination/ filetype[str(filename.suffix)]).mkdir(parents=True, exist_ok=True)
                shutil.copy(files_path/ str(filename.name), destination/ filetype[str(filename.suffix)])
                shutil.copy(files_path/ str(filename.name), rawpath)
                print(f"Added {str(filename.suffix)} as {typeinput}")
        for file in files_path.iterdir():
            f_dir=Path(files_path/ str(file.name))
            f_dir.unlink()
     
    #copy to target
    elif copymove.lower().strip()=="copy":
        for filename in files_path.iterdir():
            if str(filename.suffix) in filetype:
                Path(destination/ filetype[str(filename.suffix)]).mkdir(parents=True, exist_ok=True)
                shutil.copy(files_path/ str(filename.name), destination/ filetype[str(filename.suffix)])
            else:
                typeinput=input(f"What is the type of file called with '{str(filename.suffix)}' extension ?")
                filetype[str(filename.suffix)]=typeinput
                Path(destination/ filetype[str(filename.suffix)]).mkdir(parents=True, exist_ok=True)
                shutil.copy(files_path/ str(filename.name), destination/ filetype[str(filename.suffix)])
                print(f"Added {str(filename.suffix)} as {typeinput}")
    else:
         print("Invalid command")
         transporter()

#Some commands
def repeat():
    rawpath=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Backup")
    fp=input("Enter the directory to sort: ")
    files_path=Path(fp)
    dp=input("Enter the destination for sorted files: ")
    destination=Path(dp)
    if not fp:
        files_path=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Raw")
    if not dp:
        destination=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Data")

    #loading dictionaries that tell which extension refers to which type of file
    dict_path=Path('C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/file_dict.json')
    filetype=dict()
    with open(dict_path,'r') as file:
            filetype=json.load(file)
    transporter()

        
def restore():
    for rawfile in rawpath.iterdir():
         shutil.move(rawpath/ str(rawfile.name), files_path)
    for datafile in destination.iterdir():
         shutil.rmtree(destination/ str(datafile))
def quantity(dirs):
     for dir in dirs.iterdir():
          for i,q in enumerate(dir.iterdir(),start=1):
               continue
          print(f"{dir.stem}={i}")
def tree(dirs):
    dir_tree=dict()
    for dir in dirs.iterdir():
          dir_tree[str(dir.stem)]=[str(f.name) for f in dir.iterdir()]
    print(f"\n{str(destination.stem)}")
    for folder in dir_tree:
         print(f"->{folder}")
         for item in dir_tree[folder]:
              print(f"  ->{item}")
transporter()
#Command getter
while True:
    cmd=input("Enter command here: ")
    if cmd.strip().lower()=='exit':
         break
    elif cmd.strip().lower()=="quantity":
        quantity(destination)
    elif cmd.strip().lower()=="repeat":
         repeat()
    elif cmd.strip().lower()=="tree":
            tree(destination)
    elif cmd.strip().lower()=="restore":
            restore()
    else:
         print("Invalid command.")
          
with open(dict_path,'w') as file:
     json.dump(filetype,file)
         

        

