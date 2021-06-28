from math import sqrt


# Task 11.9.1
def forward_no_normalization(v):
    D = {}
    while len(v) > 1:
        k = len(v)
        vnew = [(v[2*i]+v[2*i+1])/2 for i in range(k//2)]
        w = [v[2*i]-v[2*i+1] for i in range(k//2)]
        D.update({(k//2, i): w[i] for i in range(k//2)})
        v = vnew
    D[(0, 0)] = v[0]
    return D


v = [1, 2, 3, 4]
print(forward_no_normalization(v))
v = [4, 5, 3, 7, 4, 5, 2, 3, 9, 7, 3, 5, 0, 0, 0, 0]
print(forward_no_normalization(v))
print()


# Task 11.9.2
def normalize_coefficients(n, D):
    return {key: value*sqrt(n/(4*key[0])) if key != (0, 0) else value * sqrt(n) for key, value in D.items()}


print(normalize_coefficients(4, {(2, 0): 1, (2, 1): 1, (1, 0): 1, (0, 0): 1}))
print(normalize_coefficients(4, forward_no_normalization([1, 2, 3, 4])))
print()


# Task 11.9.3
def forward(v):
    return normalize_coefficients(len(v), forward_no_normalization(v))


print(forward([1, 2, 3, 4]))
print()


# Task 11.9.4
def suppress(D, threshold):
    return {key: value if abs(value) >= threshold else 0 for key, value in D.items()}


print(suppress(forward([1, 2, 3, 4]), 1))
print()


# Task 11.9.5
def sparsity(D):
    return 1 - (list(D.values()).count(0)/len(D))


D = forward([1, 2, 3, 4])
print(sparsity(D))
print(sparsity(suppress(D, 1)))











