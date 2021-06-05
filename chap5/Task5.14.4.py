import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import listlist2mat
from module.GF2 import one
from module.vec import Vec
from module.mat import Mat

def find_error(c):
    H = listlist2mat([[0, 0, 0, one, one, one, one],
                 [0, one, one, 0, 0, one, one],
                 [one, 0, one, 0, one, 0, one]])
    e = H * c
    res = 0
    temp = 1
    for x in e.D:
        if e[len(e.D) - x - 1] == one:
            res += temp
        temp *= 2
    return Vec(c.D, {res - 1: one})


c = Vec({0, 1, 2, 3, 4, 5, 6}, {0:one, 2:one, 3:one, 5:one, 6:one})
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): 0, (3, 2): one,
    (0, 0): 0, (3, 0): one, (0, 4): 0, (1, 4): 0, (2, 6): one, (0, 5): 0,
    (2, 1): one, (2, 5): 0, (2, 0): one, (1, 0): one, (3, 5): 0, (0, 1): 0,
    (0, 2): 0, (3, 3): one, (0, 6): one, (3, 4): 0, (3, 1): one, (1, 6): one,
    (1, 1): one, (1, 5): one, (3, 6): one, (2, 2): 0, (1, 3): one, (2, 3): one,
    (0, 3): 0, (2, 4): one})
print(R * (find_error(c) + c))
