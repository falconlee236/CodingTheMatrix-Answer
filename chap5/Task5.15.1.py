import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.image_mat_util import file2mat, mat2display

file = file2mat("img01.png")
mat2display(file[0], file[1])