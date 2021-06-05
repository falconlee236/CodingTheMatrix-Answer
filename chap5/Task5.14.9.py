import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.bitutil import bits2mat, bits2str, str2bits, mat2bits, noise

s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
e = noise(p, 0.02)
print((mat2bits(p + e)))
print(s)
