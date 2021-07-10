from cancer_data import read_training_data
from matutil import rowdict2mat, mat2rowdict
from vec import Vec
import simplex
import random


features = {'area(worst)', 'smoothness(worst)', 'texture(mean)'}
A, b = read_training_data("../src/data/train.data", features)
print("Task 14.13.1")
# Task 14.13.1


def main_constraint(i, a_i, d_i, features):
    if d_i > 0:
        return Vec(features | {"gamma"} | A.D[0], dict(a_i.f.items() | {i: 1, "gamma": -1}.items()))
    else:
        return Vec(features | {"gamma"} | A.D[0], dict((-1 * a_i).f.items() | {i: 1, "gamma": 1}.items()))


# 861799
print("Task 14.13.2")
# Task 14.13.2


def make_matrix(feature_vectors, diagnoses, features):
    res = {}
    for key, value in feature_vectors.items():
        res[key] = main_constraint(key, value, diagnoses[key], features)
        res[-key] = Vec(res[key].D, {key: 1})
    return rowdict2mat(res)


A = make_matrix(mat2rowdict(A), b, features)


print("Task 14.13.3")
# Task 14.13.3


def make_b(A):
    return Vec(A.D[0], {key: 1 if key > 0 else 0 for key in A.D[0]})


print("Task 14.13.4")
# Task 14.13.4


def make_c(A, features):
    return Vec(A.D[1], {key: 1 for key in A.D[1] if key not in {'gamma'} | features})


print("Task 14.13.5")
# Task 14.13.5
b = make_b(A)
c = make_c(A, features)
rand_list = list(A.D[0])
random.shuffle(rand_list)
sublist = []
for i in range(len(A.D[1])):
    sublist.append(rand_list[i])
    sublist.append(-rand_list[i])
    if(len(set(sublist)) == len(A.D[1])):
        break
R_square = set(sublist)
simplex.find_vertex(A, b, R_square)
x_hat = simplex.optimize(A, b, c, R_square)


print("Task 14.13.6")
# Task 14.13.6


def C(feature_vector, x_hat):
    gamma = x_hat['gamma']
    w = Vec(features, {key: x_hat[key] for key in features})
    return 1 if w * feature_vector > gamma else -1


# Task 14.13.7
A_origin, b_origin = read_training_data("../src/data/train.data", features)
error_vec = Vec(b_origin.D, {key: C(value, x_hat) for key, value in mat2rowdict(A_origin)})
print(error_vec * b_origin)

















