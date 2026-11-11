import os
import platform
import subprocess
from pathlib import Path

print (f"Testing 123")
#Godzilla is neat
def open_os_file_manager(directory: Path) -> None:
    """Open a folder in the OS file manager. This cannot return a user selection."""
    system = platform.system().casefold()

    if os.name in ("nt", "ce"):
        os.startfile(os.path.normpath(directory))
    elif "darwin" in system:
        subprocess.run(["open", str(directory)], check=True)
    else:
        subprocess.run(["xdg-open", str(directory)], check=True)


def find_chd(rompath: Path) -> list[Path]:
    """Scan a directory (and subdirectories) for .chd files and return their paths."""
    chd_files: list[Path] = []

    # rglob walks the tree; suffix.lower() also matches .CHD on Linux
    for file_path in rompath.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() == ".chd":
            chd_files.append(file_path)

    return chd_files


def convert_chd_to_cue(chd_file: Path) -> None:
    """Extract a CHD to a .cue/.bin pair with chdman. --force overwrites existing output."""
    cue_file = chd_file.with_suffix(".cue")
    # A list of args (no shell=True) keeps paths with spaces/quotes safe
    subprocess.run(
        ["chdman", "extractcd", "-i", str(chd_file), "-o", str(cue_file), "--force"],
        check=True,
    )
    print(f"Converted {chd_file} to {cue_file}")


if __name__ == "__main__":
    rominput = input("Paste your PSX ROM directory: ").strip()
    rompath = Path(rominput)

    if not rompath.is_dir():
        print(f"Not a directory: {rompath}")
        raise SystemExit(1)

    chd_list = find_chd(rompath)

    if not chd_list:
        print("No CHD files found")
    else:
        for gamefile in chd_list:
            convert_chd_to_cue(gamefile)
        # Optional: uncomment to browse the folder after conversion
        # open_os_file_manager(rompath)
