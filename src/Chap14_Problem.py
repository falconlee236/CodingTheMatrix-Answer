from mat import Mat
from vec import Vec
from solver import solve


print("# Probem 14.16.2")
# Probem 14.16.2


def find_move_helper(A, r):
    return solve(A, Vec(A.D[0], {r: 1}))


A = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 1): 1, (1, 2): 1, (2, 2): 1, (2, 3): 1, (3, 1): 1, (3, 3): 1})
print(find_move_helper(A, 3))


print("# Problem 14.16.3")
# Problem 14.16.3


def find_move_direction(A, x, r):
    return find_move_helper(A, r)


x = Vec({1, 2, 3}, {1: 2, 2: 4, 3: 6})
print(find_move_direction(A, x, 3))















