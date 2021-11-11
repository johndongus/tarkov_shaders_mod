**Note if you are having issues running test.py, primarly a blank output. Use test-fix.py**

### Tarkov Shaders "Mod"
![Image](https://cdn.discordapp.com/attachments/774432062367203328/903140988107780156/unknown.png)

# Usage:
```
Download and unpack shaders.rar into directory with script or exe
Run scrambler.py OR test.py/exe, test includes color picker
```

# No-recoil usage
```
Copy playersuperior.bundle from `C:\Battlestate Games\eftlive\EscapeFromTarkov_Data\StreamingAssets\Windows\assets\content\commonprefabs`
Run norecoil.py, file should update in file explorer
```
 
# Manual install
![Image](https://cdn.discordapp.com/attachments/908025136395993118/908026076016558100/unknown.png)
```
git clone https://github.com/johndongus/tarkov_shaders_mod/
cd tarkov_shaders_mod
pip3 install UnityPy dearpygui
```

```
python test.py
```
*Make sure file "shaders" from downloaded rar file is in same folder as test.py*
Generates new file using colorpicker (this is the best option)
This will generate a file named `output-shaders(rename-me)`


## Errors
`AttributeError: 'Environment' object has no attribute 'file'. Did you mean: 'files'?` - **This means that the file `shaders` does not exist in the same directory as the color picker**

