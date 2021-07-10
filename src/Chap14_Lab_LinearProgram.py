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
a_i = mat2rowdict(A)[861799]
b_i = b[861799]
print(main_constraint(861799, a_i, b_i, features))


print("Task 14.13.2")
# Task 14.13.2


def make_matrix(feature_vectors, diagnoses, features):
    res = {}
    for key, value in feature_vectors.items():
        res[key] = main_constraint(key, value, diagnoses[key], features)
        res[-key] = Vec(res[key].D, {key: 1})
    return rowdict2mat(res)


A = make_matrix(mat2rowdict(A), b, features)

































