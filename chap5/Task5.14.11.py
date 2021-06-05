import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.bitutil import bits2mat, bits2str, str2bits, mat2bits, noise
from module.matutil import listlist2mat
from module.GF2 import one
from module.mat import Mat

s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}),
        {(3, 2): one, (2, 4): one, (1, 5): one, (0, 6): one})
C = G * p
e = noise(p, 0.02)
CTILDE = C + G * e
print(bits2str(mat2bits(R * CTILDE)))
