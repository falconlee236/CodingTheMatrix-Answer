from vecutil import list2vec
from independence import is_independent
from GF2 import one
from random import randint


a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])


def randGF2():
    return randint(0, 1) * one


# Task 8.7.1
def choose_secret_vector(s, t):
    while True:
        u = list2vec([randGF2() for i in range(6)])
        if a0 * u == s and b0 * u == t:
            return u


# Task 8.7.2
while True:
    flag = False
    vec_list = [(a0, b0)] + [(list2vec([randGF2() for x in range(6)]), list2vec([randGF2() for y in range(6)])) for i in range(3)]
    for i in range(2):
        for j in range(i + 1, 3):
            for k in range(j + 1, 4):
                res_list = [vec_list[i][0], vec_list[i][1], vec_list[j][0], vec_list[j][1], vec_list[k][0], vec_list[k][1]]
                if is_independent(res_list) is False:
                    flag = True
    if flag is False:
        res = {1: (res_list[0], res_list[1]), 2: (res_list[2], res_list[3]), 3: (res_list[4], res_list[5])}
        break
print(res)