from vecutil import zero_vec, list2vec
from GF2 import one
from vec import Vec


# Problem 8.9.3
def is_echelon(A):
    pivot = -1
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != 0:
                if pivot >= j:
                    return False
                pivot = j
                break
    return True


print(is_echelon([[2, 1, 0], [0, -4, 0], [0, 0, 1]]))
print(is_echelon([[2, 1, 0], [-4, 0, 0], [0, 0, 1]]))
print(is_echelon([[2, 1, 0], [0, 3, 0], [1, 0, 1]]))
print(is_echelon([[1, 1, 1, 1, 1], [0, 2, 0, 1, 3], [0, 0, 0, 5, 3]]))
print(is_echelon([[0, 2, 3, 0, 5, 6], [0, 0, 1, 0, 3, 4], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))


# Problem 8.9.6
def echelon_solve(rowlist, label_list, b):
    '''
    def triangular_solve(rowlist, label_list, b)
        D = rowlist[0].D
        x = zero_vec(D)
        for j in reversed(range(len(D))):
            c = label_list[j]
            row = rowlist[j]
            x[c] = (b[j] - x*row)/row[c]
        return x
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        if row == zero_vec(D):
            continue
        for k in range(len(row.D)):
            if row[label_list[k]] != 0:
                c = label_list[k]
                break
        x[c] = (b[j] - x*row)/row[c]
    return x


D = {'A', 'B', 'C', 'D', 'E'}
label_list = ['A', 'B', 'C', 'D', 'E']
''' Test case 1 '''
rowlist = [Vec(D, {'A': one, 'C': one, 'D': one}), Vec(D, {'B': one, 'E': one}), Vec(D, {'C': one, 'E': one}), Vec(D, {'E': one})]
b = [one, 0, one, one]
print(echelon_solve(rowlist, label_list, b))

''' Test case 2 '''
rowlist = [Vec(D, {'A': one, 'B': one, 'D': one}), Vec(D, {'B': one, 'D': one, 'E': one}), Vec(D, {'C': one, 'E': one}), Vec(D, {})]
b = [one, 0, one, 0]
print(echelon_solve(rowlist, label_list, b))








