import subprocess
import os


#path = input("Please Provide the folder where your .chd files are")


def convertchdtocue(path,filetype):
    subprocess.run(f'chdman extractcd -i "{path}.{filetype}" -o "{path}.cue" --force', shell=True)
