import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat
from math import sin, cos, pi
def identity():
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1})

def rotation(theta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'):cos(theta), ('x', 'y'):sin(theta),
                ('y', 'x'): -sin(theta), ('y', 'y'): cos(theta), ('u', 'u'): 1})

def translation(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1, ('x', 'u'): alpha, ('y', 'u'): beta})

def rotation_about(theta, x, y):
    return identity() * translation(-x, -y) * rotation(theta) * translation(x, y)

M = file2mat("img01.png")
M = (translation(1000, 500) * M[0], M[1])
V = (rotation_about(pi/6, 0, 0) * M[0], M[1])
mat2display(V[0], V[1])


