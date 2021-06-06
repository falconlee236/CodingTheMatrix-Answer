import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat

def scale(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): alpha, ('y', 'y'): beta, ('u', 'u'): 1})

M = file2mat("img01.png")
V = (scale(10, 4) * M[0], M[1])
mat2display(V[0], V[1])


