from mat import Mat
from vec import Vec
from math import sqrt


print("# Problem 11.11.1")
# Problem 11.11.1


def orthogonal_vec2rep(Q, b):
    return b * Q.transpose()


Q = Mat((set(range(3)), set(range(3))), {(0, 0): 1/sqrt(2), (0, 1): 1/sqrt(2),
                                         (1, 0): 1/sqrt(3), (1, 1): -1/sqrt(3), (1, 2): 1/sqrt(3),
                                        (2, 0): -1/sqrt(6), (2, 1): 1/sqrt(6), (2, 2): 2/sqrt(6)})
b = Vec({0, 1, 2}, {0: 10, 1: 20, 2: 30})
print(orthogonal_vec2rep(Q, b))




















