from matutil import listlist2mat, rowdict2mat, coldict2mat, mat2coldict, mat2rowdict
from mat import Mat
from vec import Vec


# Problem 5.17.12
def lin_comb_mat_vec_mult(M, v):
    vec = Vec(v.D, {})
    for key, value in mat2coldict(M).items():
        vec += (v[key] * value)
    return vec


# Problem 5.17.13
def lin_comb_vec_mat_mult(v, M):
    vec = Vec(M.D[1], {})
    for key, value in mat2rowdict(M).items():
        vec += (v[key] * value)
    return vec


# Problem 5.17.14
def dot_product_mat_vec_mult(M, v):
    return Vec(v.D, {key: v * value for key, value in mat2rowdict(M).items()})


# Problem 5.17.15
def dot_product_vec_mat_mult(v, M):
    return Vec(M.D[1], {key: v * value for key, value in mat2coldict(M).items()})


M = listlist2mat([[-1, 1, 2], [1, 2, 3], [2, 2, 1]])
v = Vec({0, 1, 2}, {0: 1, 1: 2, 2: 0})
print(lin_comb_mat_vec_mult(M, v))
print(dot_product_mat_vec_mult(M, v))

M = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
v = Vec({0, 1, 2, 3}, {0: 4, 1: 3, 2: 2, 3: 1})
print(lin_comb_vec_mat_mult(v, M))
print(dot_product_vec_mat_mult(v, M))


# Problem 5.17.16
def Mv_mat_mat_mult(A, B):
    return coldict2mat({key: A * value for key, value in mat2coldict(B).items()})


# Problem 5.17.17
def vM_mat_mat_mult(A, B):
    return rowdict2mat({key: value * B for key, value in mat2rowdict(A).items()})


''' Problem 5.17.16 Test '''
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(Mv_mat_mat_mult(A, B) == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})) # True
C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(Mv_mat_mat_mult(C, D) == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})) # True

''' Problem 5.17.17 Test '''
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(vM_mat_mat_mult(A, B) == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})) # True
C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(vM_mat_mat_mult(C, D) == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})) # True


# Problem 5.17.18
with open('UN_voting_data.txt', 'r') as file:
    temp = file.readlines()

data = []
for lines in temp:
    line = lines.split()
    data.append(line)
voting_data = {x[0]: list(map(int, x[1:len(x) - 1])) for x in data}
data_set = set(range(len(voting_data['Italy'])))
voting_data = coldict2mat({key: Vec(data_set, {x: y for x, y in enumerate(value)}) for key, value in voting_data.items()})
M = voting_data.transpose() * voting_data

result = sorted([(value, key) for key, value in M.f.items()])
# Question 1
print(result[0])
# Question 2
print(result[:10])
# Question 3
print(result[-1])


# Problem 5.17.19
def dictlist_helper(dlist, k):
    return [d[k] for d in dlist]


print(dictlist_helper([{'a': 'apple', 'b': 'bear'}, {'a': 1, 'b': 2}], 'a'))
