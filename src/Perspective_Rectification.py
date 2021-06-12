from vec import Vec
from mat import Mat
from matutil import rowdict2mat, mat2coldict, coldict2mat
from vecutil import list2vec
from solver import solve
import image_mat_util


# Task 6.12.1
def move2board(y):
    return Vec(y.D, {key: value / y['y3'] for key, value in y.f.items()})


print(move2board(Vec({'y1', 'y2', 'y3'}, {'y1': 3, 'y2': 7, 'y3': 0.2})))


# Task 6.12.2
def make_equations(x1, x2, w1, w2):
    D = [(a, b) for a in ['y1', 'y2', 'y3'] for b in ['x1', 'x2', 'x3']]
    u = [-x1, -x2, -1, 0, 0, 0, w1*x1, w1*x2, w1]
    v = [0, 0, 0, -x1, -x2, -1, w2*x1, w2*x2, w2]
    return [Vec(set(D), {D[i]: u[i] for i in range(9)}), Vec(set(D), {D[i]: v[i] for i in range(9)})]


# Task 6.12.3
w = Vec({(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}, {('y1', 'x1'): 1})


# Task 6.12.4
L = rowdict2mat({0: make_equations(358, 36, 0, 0)[0], 1: make_equations(358, 36, 0, 0)[1],
                2: make_equations(329, 597, 0, 1)[0],  3: make_equations(329, 597, 0, 1)[1],
                4: make_equations(592, 157, 1, 0)[0],  5: make_equations(592, 157, 1, 0)[1],
                6: make_equations(580, 483, 1, 1)[0],  7: make_equations(580, 483, 1, 1)[1],
                8: w})
b = list2vec([0, 0, 0, 0, 0, 0, 0, 0, 1])
h = solve(L, b)
H = Mat(({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), h.f)
print(H)


# Task 6.12.5
(X_pts, colors) = image_mat_util.file2mat('board.png', ('x1', 'x2', 'x3'))


# Task 6.12.6
Y_pts = H * X_pts


# Task 6.12.7
def mat_move2board(Y):
    return coldict2mat({key: move2board(value) for key, value in mat2coldict(Y).items()})


Y_board = mat_move2board(Y_pts)


# Task 6.12.8
image_mat_util.mat2display(Y_board, colors, ('y1', 'y2', 'y3'), scale=100, xmin=None, ymin=None)
