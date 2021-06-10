import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.vec import Vec


# Task 6.12.1
def move2board(y):
    return Vec(y.D, {key: value / y['y3'] for key, value in y.f.items()})


print(move2board(Vec({'y1', 'y2', 'y3'}, {'y1': 3, 'y2': 7, 'y3': 0.2})))


# Task 6.12.2
def make_equations(x1, x2, w1, w2):
    D = [(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}]
    u = [-x1, -x2, -1, 0, 0, 0, w1*x1, w1*x2, w1]
    v = [0, 0, 0, -x1, -x2, -1, w2*x1, w2*x2, w2]
    return [Vec(set(D), {D[i]: u[i] for i in range(9)}), Vec(set(D), {D[i]: v[i] for i in range(9)})]


# Task 6.12.3
w = Vec({(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}, {('y1', 'x1'): 1})