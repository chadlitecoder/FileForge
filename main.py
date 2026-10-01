from pathlib import Path
import shutil 
import json
print("\n LEAVE EMPTY IF DEFAULT PATHS ARE TO BE USED \n")
fp=input("Enter the directory to sort: ")
files_path=Path(fp)
dp=input("Enter the destination for sorted files: ")
destination=Path(dp)
if not fp:
    files_path=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Raw")
if not dp:
    destination=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Data")

dict_path=Path('C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/file_dict.json')
filetype=dict()

with open(dict_path,'r') as file:
        filetype=json.load(file)
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
with open(dict_path,'w') as file:
     json.dump(filetype,file)
         

        

