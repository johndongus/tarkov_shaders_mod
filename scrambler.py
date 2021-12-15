import os
from random import randbytes
inputFile = "shaders"
orginalShaderBytes = 64898506;
os.truncate(inputFile,orginalShaderBytes)
with open(inputFile, "ab") as f:
    f.write(randbytes(9999999))
os.truncate(inputFile,orginalShaderBytes)

print('Finished bitch!')
