from factoring_support import intsqrt, gcd


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































