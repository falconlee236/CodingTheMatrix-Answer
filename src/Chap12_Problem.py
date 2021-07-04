from mat import Mat
from vecutil import list2vec
from matutil import listlist2mat
from svd import factor


# Problem 12.8.1
def squared_Frob(A):
    return sum([A[x] * A[x] for x in A.f])


print(squared_Frob(listlist2mat([[1, 2, 3, 4], [-4, 2, -1, 0]])))


# Problem 12.8.7
def SVD_solve(U, Sigma, V, b):
    try:
        answer = V * Mat(Sigma.D, {key: 1/value for key, value in Sigma.f.items()}) * U.transpose() * b
    except ZeroDivisionError:
        return "FAIL"
    else:
        return answer


A = listlist2mat([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
U, Sigma, V = factor(A)
b = list2vec([2, 3, 3])
print(SVD_solve(U, Sigma, V, b))

A = listlist2mat([[1, 1, 1], [1, 1, 1], [0, 1, 1]])
U, Sigma, V = factor(A)
b = list2vec([2, 3, 3])
print(SVD_solve(U, Sigma, V, b))

















