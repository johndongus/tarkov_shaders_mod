import sys
from random import randbytes


with open(sys.argv[1], "ab") as f:
    f.write(randbytes(9999999))