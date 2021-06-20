from matutil import listlist2mat


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