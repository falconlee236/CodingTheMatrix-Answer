import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.bitutil import bits2mat, bits2str, str2bits, mat2bits

s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
print(bits2str(mat2bits(p)) == s)

for x, y in p.f.items():
    print(f"key = {x} value = {y}")
print(p)
