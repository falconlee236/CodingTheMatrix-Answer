from cancer_data import read_training_data
from vec import Vec


# Task 9.4.1
A, b = read_training_data("train.data")


# Task 9.4.2
def signum(u):
    return Vec(u.D, {key: 1 if u[key] >= 0 else -1 for key in u.D})


print(signum(Vec({'A', 'B'}, {'A': 3, 'B': -2})))
print(signum(Vec({1, 2, 3}, {1: 2, 2: -1})) == Vec({1, 2, 3}, {1: 1, 2: -1, 3: 1}))


# Task 9.4.3
def fraction_wrong(A, b, w):
    m = signum(A * w)
    length = len(m.D)
    k = m * b
    return (length - k) / (2 * length)


print(fraction_wrong(A, b, Vec(A.D[1], {x: -1 for x in A.D[1]})))


# Task 9.4.4
def loss(A, b, w):
    return (A * w - b) * (A * w - b)


print(loss(A, b, Vec(A.D[1], {x: -1 for x in A.D[1]})))


# Task 9.4.9
def find_grad(A, b, w):
    return 2 * (A * w - b) * A


print(find_grad(A, b, Vec(A.D[1], {x: -1 for x in A.D[1]})))


# Task 9.4.10
def gradient_descent_step(A, b, w, sigma):
    return w - sigma * (find_grad(A, b, w))


# Task 9.4.11
def gradient_descent(A, b, w, sigma, T):
    for i in range(T):
        w = gradient_descent_step(A, b, w, sigma)
        if i % 30 == 0:
            print(loss(A, b, w))
            print(fraction_wrong(A, b, w))


# Task 9.4.12
print("Test case 1")
print(gradient_descent(A, b, Vec(A.D[1], {x: 1 for x in A.D[1]}), 2e-9, 100))
print("Test case 2")
print(gradient_descent(A, b, Vec(A.D[1], {x: 1 for x in A.D[1]}), 1e-9, 100))
print("Test case 3")
print(gradient_descent(A, b, Vec(A.D[1], {x: 0 for x in A.D[1]}), 2e-9, 100))
print("Test case 4")
print(gradient_descent(A, b, Vec(A.D[1], {x: 0 for x in A.D[1]}), 1e-9, 10000))

# Task 9.4.13
A, b = read_training_data("validate.data")
print(gradient_descent(A, b, Vec(A.D[1], {x: 0 for x in A.D[1]}), 1e-9, 10000))



















