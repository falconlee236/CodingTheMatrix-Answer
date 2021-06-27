from vecutil import list2vec
from orthonormalization import orthonormalize, aug_orthonormalize


# Problem 10.11.9
L = list(map(list2vec, [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]))
for x in orthonormalize(L):
    print(x)






















