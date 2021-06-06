import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat
from math import sin, cos, pi

def rotation(theta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'):cos(theta), ('x', 'y'):-sin(theta),
                ('y', 'x'): sin(theta), ('y', 'y'): cos(theta), ('u', 'u'): 1})

M = file2mat("img01.png")
V = (rotation(pi/3) * M[0], M[1])
mat2display(V[0], V[1])


