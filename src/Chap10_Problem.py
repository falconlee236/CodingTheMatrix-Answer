from vecutil import list2vec
from orthogonalization import orthogonalize


L = list(map(list2vec, [[0, 0, 3, 2], [1, 2, 3, -1], [1, 2, 0, 1], [3, 1, 0, -1], [-1, -2, 3, 1]]))
L = list(map(list2vec, [[-4, 3, 1, -2], [-2, 2, 3, -1]]))
for x in orthogonalize(L):
    print(x)