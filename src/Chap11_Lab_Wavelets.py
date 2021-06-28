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



































