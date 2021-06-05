import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import listlist2mat
from module.GF2 import one
from module.vec import Vec

G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
v = Vec({0, 1, 2, 3}, {0: one, 3: one})
print(G*v)
