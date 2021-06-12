from matutil import listlist2mat, mat2coldict, mat2rowdict
from vec import Vec


# Problem 5.17.12
def lin_comb_mat_vec_mult(M, v):
    vec = Vec(v.D, {})
    for key, value in mat2coldict(M).items():
        vec += (v[key] * value)
    return vec


# Problem 5.17.13
def lin_comb_vec_mat_mult(v, M):
    vec = Vec(M.D[1], {})
    for key, value in mat2rowdict(M).items():
        vec += (v[key] * value)
    return vec


# Problem 5.17.14
def dot_product_mat_vec_mult(M, v):
    return Vec(v.D, {key: v * value for key, value in mat2rowdict(M).items()})


# Problem 5.17.14
def dot_product_vec_mat_mult(v, M):
    return Vec(M.D[1], {key: v * value for key, value in mat2coldict(M).items()})


M = listlist2mat([[-1, 1, 2], [1, 2, 3], [2, 2, 1]])
v = Vec({0, 1, 2}, {0: 1, 1: 2, 2: 0})
print(lin_comb_mat_vec_mult(M, v))
print(dot_product_mat_vec_mult(M, v))

M = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
v = Vec({0, 1, 2, 3}, {0: 4, 1: 3, 2: 2, 3: 1})
print(lin_comb_vec_mat_mult(v, M))
print(dot_product_vec_mat_mult(v, M))
