from image_mat_util import file2mat, mat2display
from mat import Mat
from math import sin, cos, pi, atan

# Task 5.15.1
file = file2mat("img01.png")
mat2display(file[0], file[1])


# Task 5.15.2
def identity():
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1})


M = file2mat("img01.png")
V = (identity() * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.3
def translation(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1, ('x', 'u'): alpha, ('y', 'u'): beta})


M = file2mat("img01.png")
V = (translation(1000, 4) * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.4
def scale(alpha, beta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): alpha, ('y', 'y'): beta, ('u', 'u'): 1})


M = file2mat("img01.png")
V = (scale(10, 4) * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.5
def rotation(theta):
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): cos(theta), ('x', 'y'): -sin(theta),
                ('y', 'x'): sin(theta), ('y', 'y'): cos(theta), ('u', 'u'): 1})


M = file2mat("img01.png")
V = (rotation(pi/3) * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.6
def rotation_about(theta, x, y):
    return identity() * translation(-x, -y) * rotation(theta) * translation(x, y)


M = file2mat("img01.png")
M = (translation(1000, 500) * M[0], M[1])
V = (rotation_about(pi/6, 0, 0) * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.7
def reflect_y():
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): -1, ('y', 'y'): 1, ('u', 'u'): 1})


M = file2mat("img01.png")
V = (reflect_y() * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.8
def reflect_x():
    return Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}),
               {('x', 'x'): 1, ('y', 'y'): -1, ('u', 'u'): 1})


M = file2mat("img01.png")
V = (reflect_x() * M[0], M[1])
mat2display(V[0], V[1])


# Task 5.15.9
def scale_color(r, g, b):
    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}),
               {('r', 'r'): r, ('g', 'g'): g, ('b', 'b'): b})


M = file2mat("img01.png")
V = (M[0], scale_color(1/3, 1/3, 1) * M[1])
mat2display(V[0], V[1])


# Task 5.15.10
def gray_scale():
    return Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}),
               {('r', 'r'): 77/256, ('r', 'g'): 151/256, ('r', 'b'): 28/256,
                ('g', 'r'): 77/256, ('g', 'g'): 151/256, ('g', 'b'): 28/256,
                ('b', 'r'): 77/256, ('b', 'g'): 151/256, ('b', 'b'): 28/256})


M = file2mat("img01.png")
V = (M[0], gray_scale() * M[1])
mat2display(V[0], V[1])


# Task 5.15.11
def reflect_about(x1, y1, x2, y2):
    m = (x2 - x1)/(y2 - y1)
    return identity() * translation(-x1, -y1) * rotation(-atan(m)) * reflect_x() * rotation(atan(m)) * translation(x1, y1)


M = file2mat("img01.png")
M = (translation(1000, 500) * M[0], M[1])
V = (reflect_about(1000, 500, 1500, 1000) * M[0], M[1])
mat2display(V[0], V[1])



















