from pagerank_test import small_links, A2
from vec import Vec
from math import sqrt


# Task 13.12.1
print("# Task 13.12.1")


def find_num_links(L):
    return Vec(L.D[0], {key: 1 for key in L.D[0]}) * L


print(find_num_links(small_links))


# Task 13.12.2
print(" # Task 13.12.2")


def make_Markov(L):
    num_links = find_num_links(L)
    for i in L.f:
        L[i] /= num_links[i[1]]


print(small_links)
make_Markov(small_links)
print(small_links)


# Task 13.12.3
print(" # Task 13.12.3")


def power_method(A1, k):
    v = Vec(A1.D[1], {key: 1 for key in A1.D[1]})
    for i in range(k):
        u = A1*v
        print(sqrt((v * v) / (u * u)))
        v = u
    return v


print(power_method(A2, 100))

































