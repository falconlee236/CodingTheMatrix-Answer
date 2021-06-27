from vecutil import list2vec
from matutil import coldict2mat
from orthonormalization import orthonormalize, aug_orthonormalize


print("# Problem 10.11.9")
# Problem 10.11.9
L = list(map(list2vec, [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]))
for x in orthonormalize(L):
    print(x)


print("# Problem 10.11.10")
# Problem 10.11.10
L = list(map(list2vec, [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]))
print(coldict2mat(L))

Qlist, Rlist = aug_orthonormalize(L)
print(coldict2mat(Qlist))
print(coldict2mat(Rlist))
print(coldict2mat(Qlist) * coldict2mat(Rlist))
print(coldict2mat(Qlist) * coldict2mat(Rlist) - coldict2mat(L))
















