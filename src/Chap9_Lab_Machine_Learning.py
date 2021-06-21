from cancer_data import read_training_data
from vec import Vec


# Task 9.4.1
A, b = read_training_data("train.data")


# Task 9.4.2
def signum(u):
    return Vec(u.D, {key: 1 if u[key] >= 0 else -1 for key in u.D})


print(signum(Vec({'A', 'B'}, {'A': 3, 'B': -2})))
print(signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1}))

# Task 9.4.3
def fraction_wrong(A, b, w):
    m = signum(A * w)
    l = len(m.D)
    k = m * b
    return (l - k) / (2 * l)
    













































