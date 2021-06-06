import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display
from module.mat import Mat
from module.matutil import listlist2mat

def gray_scale():
    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}),
               {('r', 'r'): 77/256, ('r', 'g'): 151/256, ('r', 'b'): 28/256,
                ('g', 'r'): 77/256, ('g', 'g'): 151/256, ('g', 'b'): 28/256,
                ('b', 'r'): 77/256, ('b', 'g'): 151/256, ('b', 'b'): 28/256})

M = file2mat("img01.png")
V = (M[0], gray_scale() * M[1])
mat2display(V[0], V[1])


