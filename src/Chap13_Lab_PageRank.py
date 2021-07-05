from pagerank_test import small_links, A2
from vec import Vec


# Task 13.12.1
print("# Task 13.12.1")


def find_num_links(L):
    return Vec(L.D[0], {key: 1 for key in L.D[0]}) * L


print(find_num_links(small_links))















































