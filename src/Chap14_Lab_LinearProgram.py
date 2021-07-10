from cancer_data import read_training_data
from matutil import rowdict2mat, mat2rowdict
from vec import Vec


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






















