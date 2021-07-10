from mat import Mat
from vec import Vec
from solver import solve


print("# Probem 14.16.2")
# Probem 14.16.2


def find_move_helper(A, r):
    return solve(A, Vec(A.D[0], {r: 1}))


A = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 1): 1, (1, 2): 1, (2, 2): 1, (2, 3): 1, (3, 1): 1, (3, 3): 1})


print("# Problem 14.16.3")
# Problem 14.16.3


def find_move_direction(A, x, r):
    return find_move_helper(A, r)


x = Vec({1, 2, 3}, {1: 2, 2: 4, 3: 6})


print("# Problem 14.16.4")
# Problem 14.16.4


def find_move(A, x, r):
    w = find_move_direction(A, x, r)
    sigma = 0
    for i in range(100):
        sigma = i
        test = list((x + sigma * w).f.values())
        if min(test) >= 0 and (min(w.f.values()) > 0 or len(list(filter(lambda x: x < 10e-10, test))) > 0):
            return sigma


print(find_move(A, x, 3))










