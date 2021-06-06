import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat
from math import sin, cos, atan, pi
def identity():
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1})

def rotation(theta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'):cos(theta), ('x', 'y'):sin(theta),
                ('y', 'x'): -sin(theta), ('y', 'y'): cos(theta), ('u', 'u'): 1})

def translation(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1, ('x', 'u'): alpha, ('y', 'u'): beta})

def reflect_x():
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): 1, ('y', 'y'): -1, ('u', 'u'): 1})

def reflect_about(x1, y1, x2, y2):
    m = (x2 - x1)/(y2 - y1)
    return identity() * translation(-x1, -y1) * rotation(-atan(m))* reflect_x() * rotation(atan(m)) * translation(x1, y1)


M = file2mat("img01.png")
M = (translation(1000, 500) * M[0], M[1])
V = (reflect_about(1000, 500, 1500, 1000) * M[0], M[1])
mat2display(V[0], V[1])


