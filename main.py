import subprocess

import os
import tkinter as tk
from tkinter import filedialog

# 1. Ask user to pick a folder
root = tk.Tk()
root.withdraw()
folder = filedialog.askdirectory(title="Select a folder")

# 2. Define file extension to look for
extension = ".chd"

# 3. List matching files
matching_files = [
    f for f in os.listdir(folder)
    if f.endswith(extension)
]

# Optional: Get full paths
full_paths = [os.path.join(folder, f) for f in matching_files]

print("Found files:")
for path in full_paths:
    print(path)


#path = input("Please Provide the folder where your .chd files are")


def convertchdtocue(path,filetype):
    subprocess.run(f'chdman extractcd -i "{path}.{filetype}" -o "{path}.cue" --force', shell=True)
