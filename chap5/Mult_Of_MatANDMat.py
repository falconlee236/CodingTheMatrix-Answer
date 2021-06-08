import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import rowdict2mat, coldict2mat, mat2coldict, mat2rowdict
from module.mat import Mat


# Problem 5.17.16
def Mv_mat_mat_mult(A, B):
    return coldict2mat({key: A * value for key, value in mat2coldict(B).items()})


# Problem 5.17.17
def vM_mat_mat_mult(A, B):
    return rowdict2mat({key: value * B for key, value in mat2rowdict(A).items()})


''' Problem 5.17.16 Test '''
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(Mv_mat_mat_mult(A, B) == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})) # True
C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(Mv_mat_mat_mult(C, D) == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})) # True

''' Problem 5.17.17 Test '''
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(vM_mat_mat_mult(A, B) == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})) # True
C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(vM_mat_mat_mult(C, D) == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})) # True