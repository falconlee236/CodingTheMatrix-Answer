import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import listlist2mat
from module.GF2 import one
from module.vec import Vec
from module.mat import Mat

'''
G = 7 * 4 Matrix
R = 4 * 7 Matrix
u = 7 * 1 Vector
v = 4 * 1 Vector

G * v = u
R * u = v

-> R * G * v = v
-> (R * G) * v = v # associated law
-> R * G = I (4 * 4 identity matrix)
'''

G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
v = Vec({0, 1, 2, 3}, {0: one, 3: one})
u = G*v
'''
Hint! -> Find unit vector of Matrix G and Leave that vector! 
'''
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(3, 2): one, (2, 4): one, (1, 5): one, (0, 6): one})
print(R * u)
