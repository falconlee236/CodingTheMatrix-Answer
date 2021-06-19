from vecutil import list2vec
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
    