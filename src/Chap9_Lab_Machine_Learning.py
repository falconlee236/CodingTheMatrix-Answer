from cancer_data import read_training_data
from vec import Vec


# Task 9.4.1
A, b = read_training_data("train.data")


# Task 9.4.2
def signum(u):
    return Vec(u.D, {key: 1 if u[key] >= 0 else -1 for key in u.D})


print(signum(Vec({'A', 'B'}, {'A': 3, 'B': -2})))

















































