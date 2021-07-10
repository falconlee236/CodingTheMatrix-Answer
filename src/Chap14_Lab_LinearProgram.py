from cancer_data import read_training_data
from matutil import rowdict2mat, mat2rowdict
from vec import Vec


features = {'area(worst)', 'smoothness(worst)', 'texture(mean)'}
A, b = read_training_data("../src/data/train.data", features)
# Task 14.13.1


def main_constraint(i, a_i, d_i, features):
    if d_i > 0:
        return Vec(features | {i, "gamma"}, dict(a_i.f.items() | {i: 1, "gamma": -1}.items()))
    else:
        a_i *= -1
        return Vec(features | {i, "gamma"}, dict(a_i.f.items() | {i: 1, "gamma": 1}.items()))


# 861799
a_i = mat2rowdict(A)[861799]
b_i = b[861799]
print(b_i)
print(main_constraint(861799, a_i, b_i, features))






































