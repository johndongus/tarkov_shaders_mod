import UnityPy
import os
from random import randbytes


src = "playersuperior.bundle" #Input file


env = UnityPy.load(src)
for obj in env.objects:
    #print(obj.path_id)
    if obj.path_id == 7120674869574017826:
        animationasset = obj.read_typetree();
        animationasset["Mask"] = 1;
        obj.save_typetree(animationasset)
        print('edited '+str(obj.path_id))
        break

    
new_file = env.file.save()
orginalSize = os.path.getsize(src);

with open(src, 'wb') as f:
    f.write(new_file)
with open(src, "ab") as f:
    f.write(randbytes(9999999))
    
os.truncate(src,orginalSize)
print('Finished!')
