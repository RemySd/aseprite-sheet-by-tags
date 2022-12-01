import os
import subprocess
import sys

# Macos default location
binaryAseLocation="/Applications/Aseprite.app/Contents/MacOS/aseprite"

# Default to fetch files
default_path = './Assets/'

if len(sys.argv) >= 2:
    default_path = sys.argv[1]

# Exclusions files
text_file = open("aseprite_to_exclude.txt", "r")
lines = text_file.readlines()
files_to_exlude = [default_path + item.replace('\n', '') for item in lines]

# To create sprite sheet from tags we create temporaries ".aseprite" files by tags
for root, directories, files in os.walk(default_path):
    for file in files:
        filePath = os.path.join(root, file)
        if '.aseprite' in filePath and filePath not in files_to_exlude:
            subprocess.run(
                [binaryAseLocation, "-b", filePath, "--save-as", filePath.replace(".aseprite", "_{tag}.tag.aseprite")]
            )

# Fetch all temporaries files and generate the sprite sheet
for root, directories, files in os.walk(default_path):
    for file in files:
        if '.tag.aseprite' in file:
            filePath = os.path.join(root, file)
            subprocess.run(
                [binaryAseLocation, "-b", filePath, "--sheet", f"{filePath.replace('.tag.aseprite', '').rstrip('_')}.png"]
            )
            os.remove(os.path.join(root, file))
