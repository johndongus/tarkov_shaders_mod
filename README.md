**Note if you are having issues running test.py, primarly a blank output. Use test-fix.py**

**EXE version of color chooser added, use at your own risk concidering its pre-compiled**

### Tarkov Shaders "Mod"
![Image](https://cdn.discordapp.com/attachments/774432062367203328/903140988107780156/unknown.png)

# Simple Method:
Download `dropinfiles.rar`, files to extract:
`dropinfiles.rar` - https://mega.nz/file/IEdD3aZJ#wOg3wvnBJ_zNpQ32ugAniuolXtA4wwr1xdC7BEyNlTM


shaders - `C:\Battlestate Games\EFT\EscapeFromTarkov_Data\StreamingAssets\Windows`

Note: File below is for no-recoil
*playersuperior.bundle* - `C:\Battlestate Games\EFT\EscapeFromTarkov_Data\StreamingAssets\Windows\assets\content\commonprefabs`




# Script Method (not needed, but safer)
![Image](https://cdn.discordapp.com/attachments/908025136395993118/908026076016558100/unknown.png)
```
git clone https://github.com/johndongus/tarkov_shaders_mod/
cd tarkov_shaders_mod
pip3 install UnityPy dearpygui
```


```
python3 test.py
*Make sure file "shaders" from downloaded rar file is in same folder as test.py*
Generates new file using colorpicker (this is the best option)
```

This will generate a file named `output-shaders(rename-me)`

## Useful info

```
Shader file packID's:
8646871023065948827 - player
9098473984068178372 - items / entites
5767049091772583961 - items / entites
```


## Errors and how to fix them
`AttributeError: 'Environment' object has no attribute 'file'. Did you mean: 'files'?` - **This means that the file `shaders` does not exist in the same directory as the color picker**

