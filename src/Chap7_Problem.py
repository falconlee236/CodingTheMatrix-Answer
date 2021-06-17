from Chap6_Problem import exchange, subset_basis
from vecutil import list2vec
from independence import rank
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






