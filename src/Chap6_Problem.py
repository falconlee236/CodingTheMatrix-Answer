from vec import Vec
from GF2 import one
from solver import solve
from vecutil import list2vec
from matutil import coldict2mat


# Problem 6.14.13
def rep2vec(u, veclist):
    return coldict2mat(veclist) * u


if __name__ == "__main__":
    print("\nProblem 6.14.13")
    ''' Testcase 1 '''
    a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
    a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
    a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
    print(rep2vec(Vec({0, 1, 2}, {0: 2, 1: 4, 2: 6}), [a0, a1, a2]))
    ''' Testcase 2 '''
    veclist = [[1, 0, 2, 0], [1, 2, 5, 1], [1, 5, -1, 3]]
    print(rep2vec(list2vec([5, 3, -2]), list(map(list2vec, veclist))))
    ''' Testcase 3 '''
    veclist = [[one, 0, one], [one, one, 0], [0, 0, one]]
    print(rep2vec(list2vec([one, one, 0]), list(map(list2vec, veclist))))


# Problem 6.14.14
def vec2rep(veclist, v):
    return solve(coldict2mat(veclist), v)


if __name__ == "__main__":
    print("\nProblem 6.14.14")
    ''' Testcase 1 '''
    a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
    a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
    a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
    print(vec2rep([a0, a1, a2], Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': -2})))
    ''' Testcase 2 '''
    veclist = [[1, 0, 2, 0], [1, 2, 5, 1], [1, 5, -1, 3]]
    print(vec2rep(list(map(list2vec, veclist)), list2vec([6, -4, 27, -3])))
    ''' Testcase 3 '''
    veclist = [[one, 0, one], [one, one, 0], [0, 0, one]]
    print(vec2rep(list(map(list2vec, veclist)), list2vec([0, one, one])))


# Problem 6.14.15
def is_superfluous(L, i):
    if len(L) == 1:
        return False
    sub_m = coldict2mat(L[:i] + L[i+1:])
    residual = L[i] - sub_m * solve(sub_m, L[i])
    if residual * residual < pow(10, -14):
        return True
    return False


if __name__ == "__main__":
    print("\nProblem 6.14.15")
    ''' Testcase 1 '''
    a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
    a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
    a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
    a3 = Vec({'a', 'b', 'c', 'd'}, {'a': 1, 'c': 3})
    print(is_superfluous([a0, a1, a2, a3], 3))
    print(is_superfluous([a0, a1, a2, a3], 0))
    print(is_superfluous([a0, a1, a2, a3], 1))
    ''' Testcase 2 '''
    veclist = [[1, 2, 3]]
    print(is_superfluous(list(map(list2vec, veclist)), 0))
    ''' Testcase 3 '''
    veclist = [[2, 5, 5, 6], [2, 0, 1, 3], [0, 5, 4, 3]]
    print(is_superfluous(list(map(list2vec, veclist)), 2))
    ''' Testcase 4 '''
    veclist = [[one, one, 0, 0], [one, one, one, one], [0, 0, 0, one]]
    print(is_superfluous(list(map(list2vec, veclist)), 2))


# Problem 6.14.16
def is_independent(L):
    if len(L) == 1:
        return True
    for i in range(len(L)):
        if is_superfluous(L, i) is True:
            return False
    return True


if __name__ == "__main__":
    print("\nProblem 6.14.16")
    ''' Testcase 1 '''
    a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
    a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
    a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
    a3 = Vec({'a', 'b', 'c', 'd'}, {'a': 1, 'c': 3})
    print(is_independent([a0, a1, a2]))
    print(is_independent([a0, a2, a3]))
    print(is_independent([a0, a1, a3]))
    print(is_independent([a0, a1, a2, a3]))
    ''' Testcase 2 '''
    veclist = [[2, 4, 0], [8, 16, 4], [0, 0, 7]]
    print(is_independent(list(map(list2vec, veclist))))
    ''' Testcase 3 '''
    veclist = [[1, 3, 0, 0], [2, 1, 1, 0], [1, 1, 4, -1]]
    print(is_independent(list(map(list2vec, veclist))))
    ''' Testcase 4 '''
    veclist = [[one, 0, one, 0], [0, one, 0, 0], [one, one, one, one], [one, 0, 0, one]]
    print(is_independent(list(map(list2vec, veclist))))


# Problem 6.14.17
def subset_basis(T):
    B = []
    for i in T:
        B.append(i)
        if is_independent(B) is False:
            B.pop()
    return B


if __name__ == "__main__":
    print("\nProblem 6.14.17")
    ''' Testcase 1 '''
    a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
    a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
    a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
    a3 = Vec({'a', 'b', 'c', 'd'}, {'a': 1, 'c': 3})
    print(subset_basis([a0, a1, a2, a3]))
    print(subset_basis([a0, a3, a1, a2]))
    ''' Testcase 2 '''
    veclist = [[1, 1, 2, 1], [2, 1, 1, 1], [1, 2, 2, 1], [2, 2, 1, 2], [2, 2, 2, 2]]
    print(subset_basis(list(map(list2vec, veclist))))
    ''' Testcase 3 '''
    veclist = [[one, one, 0, 0], [one, one, one, one], [0, 0, one, one], [0, 0, 0, one], [0, 0, one, 0]]
    print(subset_basis(list(map(list2vec, veclist))))


# Problem 6.14.18
def superset_basis(T, L):
    S = T[:]
    for i in L:
        if i in S:
            continue
        S.append(i)
        if is_independent(S) is False:
            S.remove(i)
    return S


if __name__ == "__main__":
    print("\nProblem 6.14.18")
    ''' Testcase 1 '''
    a0 = Vec({'a', 'b', 'c', 'd'}, {'a': 1})
    a1 = Vec({'a', 'b', 'c', 'd'}, {'b': 1})
    a2 = Vec({'a', 'b', 'c', 'd'}, {'c': 1})
    a3 = Vec({'a', 'b', 'c', 'd'}, {'a': 1, 'c': 3})
    print(superset_basis([a0, a3], [a0, a1, a2]))
    ''' Testcase 2 '''
    T = [[0, 5, 3], [0, 2, 2], [1, 5, 7]]
    L = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
    print(superset_basis(list(map(list2vec, T)), list(map(list2vec, L))))
    ''' Testcase 3 '''
    T = [[0, 5, 3], [0, 2, 2]]
    L = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
    print(superset_basis(list(map(list2vec, T)), list(map(list2vec, L))))
    ''' Testcase 4 '''
    T = [[0, one, one, 0], [one, 0, 0, one]]
    L = [[one, one, one, one], [one, 0, 0, 0], [0, 0, 0, one]]
    print(superset_basis(list(map(list2vec, T)), list(map(list2vec, L))))


# Problem 6.14.19
def exchange(S, A, z):
    M = S + [z]
    for i in range(len(S)):
        if S[i] not in A:
            sub_m = M[:i] + M[i+1:]
            if vec2rep(sub_m, S[i]) is not None:
                return S[i]
    return None


if __name__ == "__main__":
    ''' Testcase 1 '''
    S = [list2vec(v) for v in [[0, 0, 5, 3], [2, 0, 1, 3], [0, 0, 1, 0], [1, 2, 3, 4]]]
    A = [list2vec(v) for v in [[0, 0, 5, 3], [2, 0, 1, 3]]]
    z = list2vec([0, 2, 1, 1])
    print(exchange(S, A, z))
    ''' Testcase 2 '''
    S = [list2vec(v) for v in [[0, one, one, one], [one, 0, one, one], [one, one, 0, one], [one, one, one, 0]]]
    A = [list2vec(v) for v in [[0, one, one, one], [one, one, 0, one]]]
    z = list2vec([one, one, one, one])
    print(exchange(S, A, z))