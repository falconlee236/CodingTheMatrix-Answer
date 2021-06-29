from math import sqrt


def dictlist_helper(dlist, k):
    return [d[k] for d in dlist]


print("Task 11.9.1")


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
print("Task 11.9.2")


# Task 11.9.2
def normalize_coefficients(n, D):
    return {key: value*sqrt(n/(4*key[0])) if key != (0, 0) else value * sqrt(n) for key, value in D.items()}


print(normalize_coefficients(4, {(2, 0): 1, (2, 1): 1, (1, 0): 1, (0, 0): 1}))
print(normalize_coefficients(4, forward_no_normalization([1, 2, 3, 4])))
print()
print("Task 11.9.3")


# Task 11.9.3
def forward(v):
    return normalize_coefficients(len(v), forward_no_normalization(v))


print(forward([1, 2, 3, 4]))
print()
print("Task 11.9.4")


# Task 11.9.4
def suppress(D, threshold):
    return {key: value if abs(value) >= threshold else 0 for key, value in D.items()}


print(suppress(forward([1, 2, 3, 4]), 1))
print()
print("Task 11.9.5")


# Task 11.9.5
def sparsity(D):
    return 1 - (list(D.values()).count(0)/len(D))


D = forward([1, 2, 3, 4])
print(sparsity(D))
print(sparsity(suppress(D, 1)))
print()
print("Task 11.9.6")


# Task 11.9.6
def unnormalize_coefficients(n, D):
    return {key: value / sqrt(n/(4*key[0])) if key != (0, 0) else value / sqrt(n) for key, value in D.items()}


print(D)
print(unnormalize_coefficients(len(D), D))
print()
print("Task 11.9.7")


# Task 11.9.7
def backward_no_normalization(D):
    n = len(D)
    v = [D[(0, 0)]]
    while len(v) < n:
        res = []
        for i in range(len(v)):
            res.extend((v[i] + (D[(len(v), i)]/2), v[i] - (D[(len(v), i)]/2)))
        v = res
    return list(map(int, v))


D = forward([1, 2, 3, 4])
print(backward_no_normalization(unnormalize_coefficients(len(D), D)))
D = forward([4, 5, 3, 7, 4, 5, 2, 3, 9, 7, 3, 5, 0, 0, 0, 0])
print(backward_no_normalization(unnormalize_coefficients(len(D), D)))
print()
print("Task 11.9.8")


# Task 11.9.8
def backward(D):
    return backward_no_normalization(unnormalize_coefficients(len(D), D))


D = forward([1, 2, 3, 4])
print(backward(D))
D = forward([4, 5, 3, 7, 4, 5, 2, 3, 9, 7, 3, 5, 0, 0, 0, 0])
print(backward(D))
print()
print("Task 11.9.9")


# Task 11.9.9
def forward2d(vlist):
    D_list = [forward(v) for v in vlist]
    L_dict = {key: dictlist_helper(D_list, key) for key in D_list[0]}
    D_dict = {key: forward(value) for key, value in L_dict.items()}
    return D_dict


print(forward2d([[1, 2, 3, 4]]))
print(forward2d([[1, 2, 3, 4], [2, 3, 4, 3]]))
print()
print("Task 11.9.10")


# Task 11.9.10
def suppress2d(D_dict, threshold):
    return {key: suppress(value, threshold) for key, value in D_dict.items()}


print(suppress2d(forward2d([[1, 2, 3, 4]]), 1))
print(suppress2d(forward2d([[1, 2, 3, 4], [2, 3, 4, 3]]), 1))
print()
print("Task 11.9.11")


# Task 11.9.11
def sparsity2d(D_dict):
    res = 0
    for D in D_dict.values():
        res += list(D.values()).count(0)
    return 1 - (res/(len(D_dict) * len(D_dict[(0, 0)])))


print(sparsity2d(suppress2d(forward2d([[1, 2, 3, 4]]), 1)))
print(sparsity2d(suppress2d(forward2d([[1, 2, 3, 4], [2, 3, 4, 3]]), 1)))
print()
print("Task 11.9.12")


# Task 11.9.12
















