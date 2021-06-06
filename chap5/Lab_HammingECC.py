import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import listlist2mat, mat2coldict, coldict2mat
from module.bitutil import bits2mat, bits2str, str2bits, mat2bits, noise
from module.GF2 import one
from module.vec import Vec
from module.mat import Mat

# Task 5.14.1
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
v = Vec({0, 1, 2, 3}, {0: one, 3: one})
print(G*v)

# Task 5.14.2
'''
G = 7 * 4 Matrix
R = 4 * 7 Matrix
u = 7 * 1 Vector
v = 4 * 1 Vector

G * v = u
R * u = v

-> R * G * v = v
-> (R * G) * v = v # associated law
-> R * G = I (4 * 4 identity matrix)
'''

G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
v = Vec({0, 1, 2, 3}, {0: one, 3: one})
u = G*v
'''
Hint! -> Find unit vector of Matrix G and Leave that vector! 
'''
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(3, 2): one, (2, 4): one, (1, 5): one, (0, 6): one})
print(R * u)

# Task 5.14.3
H = listlist2mat([[0, 0, 0, one, one, one, one],
                 [0, one, one, 0, 0, one, one],
                 [one, 0, one, 0, one, 0, one]])
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
print(H*G)


# Task 5.14.4
def find_error(c):
    H = listlist2mat([[0, 0, 0, one, one, one, one],
                 [0, one, one, 0, 0, one, one],
                 [one, 0, one, 0, one, 0, one]])
    return Vec({0, 1, 2, 3, 4, 5, 6}, {key: one for key, value in mat2coldict(H).items() if value == c})


H = listlist2mat([[0, 0, 0, one, one, one, one],
                 [0, one, one, 0, 0, one, one],
                 [one, 0, one, 0, one, 0, one]])
c = Vec({0, 1, 2, 3, 4, 5, 6}, {0: one, 2: one, 3: one, 5: one, 6: one})
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): 0, (3, 2): one,
        (0, 0): 0, (3, 0): one, (0, 4): 0, (1, 4): 0, (2, 6): one, (0, 5): 0,
        (2, 1): one, (2, 5): 0, (2, 0): one, (1, 0): one, (3, 5): 0, (0, 1): 0,
        (0, 2): 0, (3, 3): one, (0, 6): one, (3, 4): 0, (3, 1): one, (1, 6): one,
        (1, 1): one, (1, 5): one, (3, 6): one, (2, 2): 0, (1, 3): one, (2, 3): one,
        (0, 3): 0, (2, 4): one})
print(R * (find_error(H * c) + c))


# Task 5.14.5
def find_error_matrix(S):
    return coldict2mat({key: find_error(value) for key, value in mat2coldict(S).items()})


print(find_error_matrix(listlist2mat([[one, 0],
                                      [one, 0],
                                      [one, one]])))

S = listlist2mat([[0, one, one, one], [0, one, 0, 0], [0, 0, 0, one]])
print(find_error_matrix(S) == Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}),
                                  {(1, 2): 0, (3, 2): one, (0, 0): 0,
                                   (4, 3): one, (3, 0): 0, (6, 0): 0,
                                   (2, 1): 0, (6, 2): 0, (2, 3): 0,
                                   (5, 1): one, (4, 2): 0, (1, 0): 0,
                                   (0, 3): 0, (4, 0): 0, (0, 1): 0,
                                   (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0,
                                   (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0,
                                   (2, 2): 0, (1, 3): 0, (5, 3): 0,
                                   (5, 2): 0, (0, 2): 0}))


# Task 5.14.6
s = ''.join([chr(i) for i in range(256)])
print(str2bits(s))
for x in str2bits(s):
    print(x)
print(bits2str(str2bits(s)))

# Task 5.14.7
s = ''.join([chr(i) for i in range(256)])
p = bits2mat(str2bits(s))
print(bits2str(mat2bits(p)) == s)

for x, y in p.f.items():
    print(f"key = {x} value = {y}")
print(p.D)

# Task 5.14.8
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
print(bits2str(mat2bits(p)) == s)

for x, y in p.f.items():
    print(f"key = {x} value = {y}")
print(p)

# Task 5.14.9
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
e = noise(p, 0.02)
print((mat2bits(p + e)))
print(s)

# Task 5.14.10
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
C = G * p
print(C.D[0])
print(C.D[1])

# Task 5.14.11
s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}),
        {(3, 2): one, (2, 4): one, (1, 5): one, (0, 6): one})
C = G * p
e = noise(p, 0.02)
CTILDE = C + G * e
print(bits2str(mat2bits(R * CTILDE)))


# Task 5.14.12, Task 5.14.13
def correct(A):
    H = listlist2mat([[0, 0, 0, one, one, one, one],
                     [0, one, one, 0, 0, one, one],
                     [one, 0, one, 0, one, 0, one]])
    return A + find_error_matrix(H * A)


s = "I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it"
p = bits2mat(str2bits(s))
G = listlist2mat([[one, 0, one, one],
                  [one, one, 0, one],
                  [0, 0, 0, one],
                  [one, one, one, 0],
                  [0, 0, one, 0],
                  [0, one, 0, 0],
                  [one, 0, 0, 0]])
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}),
        {(3, 2): one, (2, 4): one, (1, 5): one, (0, 6): one})
C = G * p
e = noise(p, 0.02)
CTILDE = C + G * e
print(bits2str(mat2bits(R * CTILDE)))
test = correct(CTILDE)
print(bits2str(mat2bits(R * test)))

