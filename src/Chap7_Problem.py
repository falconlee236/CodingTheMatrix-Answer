from Chap6_Problem import exchange, subset_basis, vec2rep, rep2vec
from vecutil import list2vec
from independence import rank, is_independent
from matutil import listlist2mat, mat2coldict
from GF2 import one


# Problem 7.7.4
def morph(S, B):
    T = S[:]
    res = []
    for x in B:
        w = exchange(T, B, x)
        res.append((x, w))
        T.append(x)
        T.remove(w)
    return res


if __name__ == "__main__":
    S = [list2vec(v) for v in [[2, 4, 0], [1, 0, 3], [0, 4, 4], [1, 1, 1]]]
    B = [list2vec(v) for v in [[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
    for (z, w) in morph(S, B):
        print(f"injecting {z}")
        print(f"ejecting {w}")
        print()


# Problem 7.7.6
def my_is_independent(L):
    return True if rank(L) == len(L) else False


if __name__ == "__main__":
    ''' Test case 1 '''
    print(my_is_independent([list2vec(v) for v in [[2, 4, 0], [8, 16, 4], [0, 0, 7]]]))
    ''' Test case 2 '''
    print(my_is_independent([list2vec(v) for v in [[1, 3, 0, 0], [2, 1, 1, 0], [0, 0, 1, 0], [1, 1, 4, -1]]]))
    ''' Test case 3 '''
    print(my_is_independent([list2vec(v) for v in [[one, 0, one, 0], [0, one, 0, 0], [one, one, one, one], [one, 0, 0, one]]]))


# Problem 7.7.7
def my_rank(L):
    return len(subset_basis(L))


if __name__ == "__main__":
    ''' Test case 1 '''
    print(my_rank([list2vec(v) for v in [[1, 2, 3], [4, 5, 6], [1.1, 1.1, 1.1]]]))
    ''' Test case 2 '''
    print(my_rank([list2vec(v) for v in [[1, 3, 0, 0], [2, 0, 5, 1], [0, 0, 1, 0], [0, 0, 7, -1]]]))
    ''' Test case 3 '''
    print(my_rank([list2vec(v) for v in [[one, 0, one, 0], [0, one, 0, 0], [one, one, one, one], [0, 0, 0, one]]]))


# Problem 7.7.11
def direct_sum_decompose(U_basis, V_basis, w):
    ans = vec2rep(U_basis + V_basis, w)
    u = list2vec([ans[i] for i in range(len(U_basis))])
    v = list2vec([ans[i] for i in range(len(U_basis), len(U_basis + V_basis))])
    return (rep2vec(u, U_basis), rep2vec(v, V_basis))


if __name__ == "__main__":
    ''' Test case1 '''
    U_basis = list(map(list2vec, [[2, 1, 0, 0, 6, 0], [11, 5, 0, 0, 1, 0], [3, 1.5, 0, 0, 7.5, 0]]))
    V_basis = list(map(list2vec, [[0, 0, 7, 0, 0, 1], [0, 0, 15, 0, 0, 2]]))
    w = list2vec([2, 5, 0, 0, 1, 0])
    print(direct_sum_decompose(U_basis, V_basis, w))
    w = list2vec([0, 0, 3, 0, 0, -4])
    print(direct_sum_decompose(U_basis, V_basis, w))
    w = list2vec([1, 2, 0, 0, 2, 1])
    print(direct_sum_decompose(U_basis, V_basis, w))
    w = list2vec([-6, 2, 4, 0, 4, 5])
    print(direct_sum_decompose(U_basis, V_basis, w))
    ''' Test case2 '''
    U_basis = list(map(list2vec, [[one, one, 0, one, 0, one], [one, one, 0, 0, 0, one], [one, 0, 0, 0, 0, 0]]))
    V_basis = list(map(list2vec, [[one, one, one, 0, one, one]]))
    w = list2vec([0, 0, 0, 0, 0, 0])
    print(direct_sum_decompose(U_basis, V_basis, w))
    w = list2vec([one, 0, 0, one, 0, 0])
    print(direct_sum_decompose(U_basis, V_basis, w))
    w = list2vec([one, one, one, one, one, one])
    print(direct_sum_decompose(U_basis, V_basis, w))


# Problem 7.7.12
def is_invertible(M):
    return True if len(M.D[0]) == len(M.D[1]) and is_independent(list(mat2coldict(M).values())) is True else False


if __name__ == "__main__":
    m1 = listlist2mat([[1, 2, 3], [3, 1, 1]])
    m2 = listlist2mat([[1, 0, 1, 0], [0, 2, 1, 0], [0, 0, 3, 1], [0, 0, 0, 4]])
    m3 = listlist2mat([[1, 0], [0, 1], [2, 1]])
    m4 = listlist2mat([[1, 0], [0, 1]])
    m5 = listlist2mat([[1, 0, 1], [0, 1, 1], [1, 1, 0]])
    m6 = listlist2mat([[one, 0, one], [0, one, one], [one, one, 0]])
    m7 = listlist2mat([[one, one], [0, one]])
    print(list(map(is_invertible, [m1, m2, m3, m4, m5, m6, m7])))


# Problem 7.7.13
def find_matrix_inverse(A):
    pass


if __name__ == "__main__":






