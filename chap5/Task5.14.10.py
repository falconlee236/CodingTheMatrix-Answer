import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.bitutil import bits2mat, bits2str, str2bits, mat2bits
from module.matutil import listlist2mat
from module.GF2 import one

s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
C = G * p
print(C.D[0])
print(C.D[1])