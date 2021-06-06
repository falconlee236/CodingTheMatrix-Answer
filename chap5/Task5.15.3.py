import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat

def translation(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1, ('x', 'u'): alpha, ('y', 'u'): beta})

M = file2mat("img01.png")
V = (translation(1000, 4) * M[0], M[1])
mat2display(V[0], V[1])


