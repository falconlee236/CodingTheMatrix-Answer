from factoring_support import intsqrt, gcd, dumb_factor, primes, prod
from echelon import transformation_rows
from GF2 import one
from vec import Vec


print("Task 8.8.1")


# Task 8.8.1
def root_method(N):
    for x in range(1, N):
        a = intsqrt(N) + x
        b = intsqrt(a * a - N)
        if isinstance(b, int):
            return a - b


print(list(map(root_method, [55, 77, 146771, 118])))


print("Task 8.8.2")
# Task 8.8.2
r = 65165321354
s = 187465732135446
t = 89798919616132138576465
a = r * s
b = s * t
d = gcd(a, b)
print(a % d == 0 and b % d == 0 and d >= s)


print("Task 8.8.3")
# Task 8.8.3
N = 367160330145890434494322103
a = 67469780066325164
b = 9429601150488992
d = gcd(a - b, N)
print((a * a - b * b) % N == 0)
print(N % d == 0)
print(d)


print("Task 8.8.4")
# Task 8.8.4
primeset = {2, 3, 5, 7, 11, 13}
print(dumb_factor(12, primeset))
print(dumb_factor(154, primeset))
print(dumb_factor(2 * 3 * 3 * 3 * 11 * 11 * 13, primeset))
print(dumb_factor(2 * 17, primeset))
print(dumb_factor(2 * 3 * 5 * 7 * 19, primeset))


print("Task 8.8.5")


# Task 8.8.5
def int2GF2(i):
    return one if i % 2 == 1 else 0


print(int2GF2(3))
print(int2GF2(4))


print("Task 8.8.6")


# Task 8.8.6
def make_Vec(primeset, factors):
    return Vec(primeset, {a: int2GF2(b) for (a, b) in factors})


print(make_Vec({2, 3, 5, 7, 11}, [(3, 1)]))
print(make_Vec({2, 3, 5, 7, 11}, [(2, 17), (3, 0), (5, 1), (11, 3)]))


print("Task 8.8.7")


# Task 8.8.7
def find_candidates(N, primeset):
    roots = []
    rowlist = []
    i = 2
    while len(roots) <= len(primeset) and len(rowlist) <= len(primeset):
        x = intsqrt(N) + i
        fact_vec = dumb_factor(x * x - N, primeset)
        if fact_vec:
            roots.append(x)
            rowlist.append(fact_vec)
        i += 1
    return roots, [make_Vec(primeset, row) for row in rowlist]


N = 2419
roots, rowlist = find_candidates(N, primes(32))
print(roots)


print("Task 8.8.8")
# Task 8.8.8
a = 53 * 77
b = 2 * 3 * 3 * 5 * 13
print(gcd(a - b, N))


print("Task 8.8.9")
# Task 8.8.9
a = 53 * 67 * 71
b = 2 * 3 * 3 * 5 * 19 * 23
print(gcd(a - b, N))


print("Task 8.8.10")


# Task 8.8.10
def find_a_and_b(v, roots, N):
    alist = [roots[i] for i in range(len(roots)) if v[i] == one]
    a = prod(alist)
    c = prod([x * x - N for x in alist])
    b = intsqrt(c)
    assert b * b == c
    return (a, b)


def find_factorization(N, M):
    for i in range(-1, -N, -1):
        try:
            res = find_a_and_b(M[i], roots, N)
        except AssertionError or ZeroDivisionError:
            continue
        else:
            g = gcd(res[0] - res[1], N)
            if g != 1:
                return res, g


N = 2419
M = transformation_rows(rowlist)
print(find_factorization(N, M))


print("Task 8.8.11")
# Task 8.8.11

N = 2461799993978700679
primeset = primes(10000)
print(1)
roots, rowlist = find_candidates(N, primeset)
print(2)
M = transformation_rows(rowlist)
print(3)
print(find_factorization(N, M))



print("Task 8.8.12")
# Task 8.8.12
N = 20672783502493917028427
primeset = primes(10000)
print(1)
roots, rowlist = find_candidates(N, primeset)
print(2)
M = transformation_rows(rowlist)
print(3)
print(find_factorization(N, M))


print("Task 8.8.13")
# Task 8.8.12
N = 20672783502493917028427
primeset = primes(10000)
print(1)
roots, rowlist = find_candidates(N, primeset)
print(2)
M_rows = transformation_rows(rowlist, sorted(primeset, reverse=True))
print(3)
print(find_factorization(N, M_rows))












