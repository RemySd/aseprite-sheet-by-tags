import os
import subprocess

# Macos default location
binaryAseLocation="/Applications/Aseprite.app/Contents/MacOS/aseprite"

# Avoir une notion d'exclusion

# Avoir une notion de build custom

# Default to fetch files
defaultPath = './Assets'

# To create sprite sheet from tags we create temporaries ".aseprite" files by tags
for root, directories, files in os.walk(defaultPath):
    for file in files:
        if '.aseprite' in file:
            filePath = os.path.join(root, file)
            subprocess.run(
                [binaryAseLocation, "-b", filePath, "--save-as", filePath.replace(".aseprite", "_{tag}.tag.aseprite")],
                capture_output=True
            )

# Fetch all temporaries files and generate the sprite sheet
for root, directories, files in os.walk(defaultPath):
    for file in files:
        if '.tag.aseprite' in file:
            filePath = os.path.join(root, file)
            subprocess.run(
                [binaryAseLocation, "-b", filePath, "--sheet", f"{filePath.replace('.tag.aseprite', '').rstrip('_')}.png"],
                capture_output=True
            )
            os.remove(os.path.join(root, file))
