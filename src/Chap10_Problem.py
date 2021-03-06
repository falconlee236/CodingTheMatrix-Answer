from vecutil import list2vec
from matutil import coldict2mat, mat2rowdict, listlist2mat
from orthonormalization import orthonormalize, aug_orthonormalize
from triangular import triangular_solve
from mat import Mat
from vec import Vec
from read_data import read_vectors
from cancer_data import read_training_data
import QR


print("\n# Problem 10.11.9")
# Problem 10.11.9
L = list(map(list2vec, [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]))
for x in orthonormalize(L):
    print(x)


print("\n# Problem 10.11.10")
# Problem 10.11.10
L = list(map(list2vec, [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]))
print(coldict2mat(L))

Qlist, Rlist = aug_orthonormalize(L)
print(coldict2mat(Qlist))
print(coldict2mat(Rlist))
print(coldict2mat(Qlist) * coldict2mat(Rlist))
print(coldict2mat(Qlist) * coldict2mat(Rlist) - coldict2mat(L))


print("\n# Problem 10.11.12")
# Problem 10.11.12


def QR_solve(A, b):
    Q, R = QR.factor(A)
    return triangular_solve(mat2rowdict(R), sorted(A.D[1], key=repr), Q.transpose() * b)


A = Mat(({'a', 'b', 'c'}, {'A', 'B'}), {('a', 'A'): -1, ('a', 'B'): 2, ('b', 'A'): 5, ('b', 'B'): 3, ('c', 'A'): 1, ('c', 'B'): -2})
print(A)

Q, R = QR.factor(A)
print(Q)
print(R)

b = Vec({'a', 'b', 'c'}, {'a': 1, 'b': -1})
x = QR_solve(A, b)
print(x)
print(A.transpose() * (b - A*x))


print("\n# Problem 10.11.15")
# Problem 10.11.15
vec_list = read_vectors('age-height.txt')
A = listlist2mat([[1, vec['age']] for vec in vec_list])
b = list2vec([vec['height'] for vec in vec_list])
print(QR_solve(A, b))


print("\n# Problem 10.11.16\n")
# Problem 10.11.16
A, b = read_training_data("train.data")
ans = QR_solve(A, b)
for x in ans.D:
    print(f'key = {x} value = {ans[x]}')

