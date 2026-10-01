from pathlib import Path
files_path=Path("C:/Users/swast/OneDrive/Desktop/Python Project/FileForge/Raw")
for filenames in files_path.iterdir():
    print(filenames.name)