from vec import Vec
from GF2 import one
from vecutil import list2vec
from matutil import coldict2mat


# Problem 6.14.14
def rep2vec(u, veclist):
    return coldict2mat(veclist) * u


''' Testcase 1 '''
a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
print(rep2vec(Vec({0, 1, 2}, {0: 2, 1: 4, 2: 6}), [a0, a1, a2]).f)
''' Testcase 2 '''
veclist = [[1, 0, 2, 0], [1, 2, 5, 1], [1, 5, -1, 3]]
print(rep2vec(list2vec([5, 3, -2]), list(map(list2vec, veclist))))
''' Testcase 3 '''
veclist = [[one, 0, one], [one, one, 0], [0, 0, one]]
print(rep2vec(list2vec([one, one, 0]), list(map(list2vec, veclist))))

