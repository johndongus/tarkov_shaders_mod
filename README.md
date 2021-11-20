**Note if you are having issues running colorpicker.py, primarly a blank output. Use colorpicker-fix.py**


new shader dumps:
https://mega.nz/file/1IUDAQjQ#v_dbnDgd6sc94enGvvneGosgP0u6PRNlQUTjaPf_B34
https://mega.nz/file/VJcHXQAA#jjG9E1eXXe_TSkTqAjyMUlqaNOHaNZOwbWBFZpJAWkI


### Tarkov Shaders "Mod"
![Image](https://cdn.discordapp.com/attachments/774432062367203328/903140988107780156/unknown.png)

# Files:
_colorpicker.py_ - **ESP color selection & file randomizationish**

_scrambler.py_ - **Randomizes asset file**

_norecoil.py_ - **Modify's existing playersuperior.bundle file to enable no-recoil** (Sketchy)

# Usage:
Download and unpack `shaders.rar` into directory with script or exe

Run `scrambler.py` **_OR_** `colorpicker.py/test.exe`, colorpicker includes color picker

# No-recoil usage

Copy `playersuperior.bundle` from `C:\Battlestate Games\eftlive\EscapeFromTarkov_Data\StreamingAssets\Windows\assets\content\commonprefabs`

Run `norecoil.py`, file should update in file explorer

 
# Manual install
![Image](https://cdn.discordapp.com/attachments/908025136395993118/908026076016558100/unknown.png)
```
git clone https://github.com/johndongus/tarkov_shaders_mod/
cd tarkov_shaders_mod
pip3 install UnityPy dearpygui
```



## Errors
`AttributeError: 'Environment' object has no attribute 'file'. Did you mean: 'files'?` - **This means that the file `shaders` does not exist in the same directory as the color picker**

