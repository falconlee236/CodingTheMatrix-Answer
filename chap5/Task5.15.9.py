import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat

def scale_color(r, g, b):
    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}),
               {('r', 'r'): r, ('g', 'g'): g, ('b', 'b'): b})

M = file2mat("img01.png")
V = (M[0], scale_color(1/3, 1/3, 1) * M[1])
mat2display(V[0], V[1])


