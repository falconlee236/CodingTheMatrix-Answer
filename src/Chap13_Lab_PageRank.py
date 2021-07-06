from pagerank_test import small_links, A2
from pagerank import find_word, read_data
from vec import Vec
from mat import Mat
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
    col_len = len(A1.D[1])
    for i in range(k):
        sub_v = 0.15 * v
        sum_v = sum(sub_v.f.values())
        A2_vec = Vec(sub_v.D, {key: sum_v / col_len for key in sub_v.D})
        u = 0.85 * A1 * v + A2_vec
        print(sqrt((v * v) / (u * u)))
        v = u
    return v


# Task 13.12.4
links = read_data("links.bin")


# Task 13.12.5


def wikigoogle(w, k, p):
    related = find_word(w)
    related.sort(key=lambda x: p[x], reverse=True)
    return related[:k]


# Task 13.12.6
make_Markov(links)
eigenvec = power_method(links, 5)
jordanlist = wikigoogle("jordan", 10, eigenvec)


# Task 13.12.7
def power_method_biased(A1, k, r):
    v = Vec(A1.D[1], {key: 1 for key in A1.D[1]})
    col_len = len(A1.D[1])
    for i in range(k):
        sub_v = 0.15 * v
        sum_v = sum(sub_v.f.values())
        Ar = 0.3 * Vec(A1.D[0], {r: sum(v.f.values())})
        A2_vec = Vec(sub_v.D, {key: sum_v / col_len for key in sub_v.D})
        u = 0.55 * A1 * v + A2_vec + Ar
        print(sqrt((v * v) / (u * u)))
        v = u
    return v


sport_biased_eigenvec = power_method_biased(links, 5, "sport")
sport_biased_jordanlist = wikigoogle("jordan", 10, sport_biased_eigenvec)
print(jordanlist)
print(sport_biased_jordanlist)














