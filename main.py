import subprocess
import os, platform
import platform
from pathlib import Path


def openOSRespectiveFM(directory: Path) -> None:
    def run_windows() -> bool:
        return os.name in ['nt', 'ce']
    def run_macOS() -> bool:
        return "darwin" in platform.system().casefold()
    
    if run_windows():
        os.startfile(os.path.normpath(directory))
    elif run_macOS:
        subprocess.run(['open',str(directory)], check = True)
    else:
        subprocess.run(['xdg-open', str(directory)], check = True)
    



def find_CHD(rompath): 
    """
    This function simply scans a directory and sub-directories and identifies all .chd files

    Returns:
    None
    """
    chd_files = [] #Initialize an Empty list

    #Iterates through all directories and sub directories looking for .chd files
    for file_path in rompath.rglob("*.chd"):
        if file_path.is_file():
            chd_files.append(file_path) #appends each file path to the list         
    return chd_files

def convert_chd_to_cue(chd_file):
    cue_file = chd_file.with_suffix('.cue') #takes the name
    subprocess.run(f'chdman extractcd -i "{chd_file}" -o "{cue_file}" --force', shell=True)
    print(f"Converted {chd_file} to {cue_file}")


# Execute Code
if __name__ == "__main__":
    #rominput = input("Paste Your PSX ROM directory: ")
    print(f'Please Select a Path: ')
    openOSRespectiveFM()
    rompath = Path(rominput) #Necessary to define the input string as a "Path" variable
    chd_list = find_CHD(rompath) #Runs the find_CHD function and assigns the output list to chd_list
    
    if not chd_list:
        print("No CHD files found")
    else:
        for gamefiles in chd_list:
            convert_chd_to_cue(gamefiles)