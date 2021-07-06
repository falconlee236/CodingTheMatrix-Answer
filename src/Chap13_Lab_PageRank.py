from pagerank_test import small_links, A2
from pagerank import find_word, read_data
from vec import Vec
from math import sqrt


# Task 13.12.1


def find_num_links(L):
    return Vec(L.D[0], {key: 1 for key in L.D[0]}) * L


# Task 13.12.2


def make_Markov(L):
    num_links = find_num_links(L)
    for i in L.f:
        L[i] /= num_links[i[1]]


make_Markov(small_links)
# Task 13.12.3


def power_method(A1, k):
    v = Vec(A1.D[1], {key: 1 for key in A1.D[1]})
    for i in range(k):
        u = A1*v
        print(sqrt((v * v) / (u * u)))
        v = u
    return v


A = 0.85 * small_links + 0.15 * A2
eigenvec = power_method(A, 10)


# Task 13.12.4
links = read_data("links.bin")


# Task 13.12.5


def wikigoogle(w, k, p):
    related = find_word(w)
    related.sort(key=lambda x: p[x], reverse=True)
    return related[:k]

























