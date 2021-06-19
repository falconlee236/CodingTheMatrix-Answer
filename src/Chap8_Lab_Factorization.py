from factoring_support import intsqrt, gcd, dumb_factor
from GF2 import one
from vec import Vec


# Task 8.8.1
def root_method(N):
    for x in range(1, N):
        a = intsqrt(N) + x
        b = intsqrt(a * a - N)
        if isinstance(b, int):
            return a - b


print(list(map(root_method, [55, 77, 146771, 118])))


# Task 8.8.2
r = 65165321354
s = 187465732135446
t = 89798919616132138576465
a = r * s
b = s * t
d = gcd(a, b)
print(a % d == 0 and b % d == 0 and d >= s)


# Task 8.8.3
N = 367160330145890434494322103
a = 67469780066325164
b = 9429601150488992
d = gcd(a - b, N)
print((a * a - b * b) % N == 0)
print(N % d == 0)
print(d)


# Task 8.8.4
primeset = {2, 3, 5, 7, 11, 13}
print(dumb_factor(12, primeset))
print(dumb_factor(154, primeset))
print(dumb_factor(2 * 3 * 3 * 3 * 11 * 11 * 13, primeset))
print(dumb_factor(2 * 17, primeset))
print(dumb_factor(2 * 3 * 5 * 7 * 19, primeset))


# Task 8.8.5
def int2GF2(i):
    return one if i % 2 == 1 else 0


print(int2GF2(3))
print(int2GF2(4))


# Task 8.8.6
def make_Vec(primeset, factors):
    return Vec(primeset, {a: int2GF2(b) for (a, b) in factors})


print(make_Vec({2, 3, 5, 7, 11}, [(3, 1)]))
print(make_Vec({2, 3, 5, 7, 11}, [(2, 17), (3, 0), (5, 1), (11, 3)]))






















