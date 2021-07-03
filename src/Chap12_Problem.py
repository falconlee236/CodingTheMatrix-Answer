from mat import Mat
from matutil import listlist2mat


# Problem 12.8.1
def squared_Frob(A):
    return sum([A[x] * A[x] for x in A.f])


print(squared_Frob(listlist2mat([[1, 2, 3, 4], [-4, 2, -1, 0]])))
