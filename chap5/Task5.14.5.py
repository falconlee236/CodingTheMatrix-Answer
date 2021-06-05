import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import *
from module.GF2 import one
from module.vec import Vec
from module.mat import Mat

def find_error(c):
    H = listlist2mat([[0, 0, 0, one, one, one, one],
                 [0, one, one, 0, 0, one, one],
                 [one, 0, one, 0, one, 0, one]])
    return Vec({0, 1, 2, 3, 4, 5, 6}, {key: one for key, value in mat2coldict(H).items() if value == c})

def find_error_matrix(S):
    return coldict2mat({key: find_error(value) for key, value in mat2coldict(S).items()})
  
print(find_error_matrix(listlist2mat([[one, 0],
                   [one, 0],
                   [one, one]])))

S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
print(find_error_matrix(S) == Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one,
        (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0,
        (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0,
        (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0,
        (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0,
        (5, 2): 0, (0, 2): 0}))