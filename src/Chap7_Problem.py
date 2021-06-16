from Chap6_Problem import exchange
from vecutil import list2vec


# Problem 7.7.4
def morph(S, B):
    T = S[:]
    res = []
    for x in B:
        w = exchange(T, B, x)
        res.append((x, w))
        T.append(x)
        T.remove(T.index(w))
    return res


S = [list2vec(v) for v in [[2, 4, 0], [1, 0, 3], [0, 4, 4], [1, 1, 1]]]
B = [list2vec(v) for v in [[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
for (z, w) in morph(S, B):
    print(f"injecting {z}")
    print(f"ejecting {w}")
    print()