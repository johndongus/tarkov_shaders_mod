##
# Use this to load modified shaders, may help with detection, may not do anything at all. I have no idea
# Usage: rename your modded shaders to `modshader` and the orginal shaders from latest patch into the same folder as this script
##
modshaders = "modshaders"
originalshaders = "ogshaders"
assetPath = "C:/Battlestate Games/EFT/EscapeFromTarkov_Data/StreamingAssets/Windows/" #MAKE SURE THIS IS CORRECT!



import psutil
from shutil import copyfile
import time

print("Waiting for game to launch");
while True:
    if "EscapeFromTarkov.exe" in (i.name() for i in psutil.process_iter()):
        print("Escape from Tarkov Started, doing stuff...")
        copyfile(modshaders, assetPath+'shaders')
        time.sleep(20)
        copyfile(originalshaders, assetPath+'shaders')
        print("Done")
        break
