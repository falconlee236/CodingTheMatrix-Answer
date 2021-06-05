import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.bitutil import bits2mat, bits2str, str2bits, mat2bits

s = ''.join([chr(i) for i in range(256)])
p = bits2mat(str2bits(s))
print(bits2str(mat2bits(p)) == s)

for x, y in p.f.items():
    print(f"key = {x} value = {y}")
print(p.D)
