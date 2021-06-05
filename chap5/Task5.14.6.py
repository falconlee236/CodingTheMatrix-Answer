import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.bitutil import str2bits, bits2str

s = ''.join([chr(i) for i in range(256)])
print(str2bits(s))
for x in str2bits(s):
    print(x)
print(bits2str(str2bits(s)))
