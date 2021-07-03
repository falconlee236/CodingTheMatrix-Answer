from eigenfaces import load_images, test_M, test_x
from image import image2display
from matutil import rowdict2mat, mat2coldict, coldict2mat, mat2rowdict
from svd import factor
from vec import Vec
import copy


# Task 12.6.1
faces_img = load_images("../img/faces")


# Task 12.6.2
def make_centerVec(imgdict):
    center = []
    vec_len = len(imgdict)
    for i in range(189):
        res_list = []
        for j in range(166):
            res = 0
            for img in imgdict.values():
                res += img[i][j]
            res_list.append(res/vec_len)
        center.append(res_list)
    return center


def make_centeringVec(imgdict, center):
    centering_img = copy.deepcopy(imgdict)
    for img in centering_img.keys():
        for i in range(189):
            for j in range(166):
                centering_img[img][i][j] -= center[i][j]
    return centering_img


center = make_centerVec(faces_img)
center_img = make_centeringVec(faces_img, center)


# Task 12.6.3
D = [(x, y) for x in range(166) for y in range(189)]
center_vec = {key: Vec(set(D), {x: value[x[1]][x[0]] for x in D}) for key, value in center_img.items()}
A = rowdict2mat(center_vec)
u, w, v = factor(A)
sub_m = mat2coldict(v)
M = coldict2mat({i: sub_m[i] for i in range(10)})


# Task 12.6.4
def projected_representation(x, M):
    return M.transpose() * x


print("Task 12.6.4")
print(projected_representation(test_x, test_M))


# Task 12.6.5
def projection_length_squared(x, M):
    n = M * projected_representation(x, M)
    return n * n


print("Task 12.6.5")
print(projection_length_squared(test_x, test_M))


# Task 12.6.6
def distance_squared(x, M):
    return x * x - projection_length_squared(x, M)


print("Task 12.6.6")
print(distance_squared(test_x, test_M))


# Task 12.6.7
distance_list = {x: distance_squared(y, M) for x, y in mat2rowdict(A).items()}
print("Task 12.6.7")
for x in distance_list:
    print(f"num = {x}  | ", end="")
    print(format(distance_list[x], ','))


# Task 12.6.8
unclass_img = load_images("../img/unclassified", n=11)
center_unclass = make_centerVec(unclass_img)
center_unclass_img = make_centeringVec(unclass_img, center_unclass)
D = [(x, y) for x in range(166) for y in range(189)]
center_unclass_vec = {key: Vec(set(D), {x: value[x[1]][x[0]] for x in D}) for key, value in center_unclass_img.items()}
B = rowdict2mat(center_unclass_vec)
distance_unclass_list = {x: distance_squared(y, M) for x, y in mat2rowdict(B).items()}
print("Task 12.6.8")
for x in distance_unclass_list:
    print(f"num = {x}  | ", end="")
    print(format(distance_unclass_list[x], ','))


# Task 12.6.10
def project(x, M):
    return M * projected_representation(x, M)


# Task 12.6.11
def face_project(D, center):
    project_list = {x: project(y, M) for x, y in mat2rowdict(D).items()}
    original_project = {key: [[value[(i, j)] for i in range(166)] for j in range(189)] for key, value in project_list.items()}
    for img in original_project.keys():
            for i in range(189):
                for j in range(166):
                    original_project[img][i][j] += center[i][j]
    return original_project


original_project = face_project(A, center)
for x in range(len(original_project)):
    image2display(original_project[x])


# Task 12.6.12
original_project = face_project(B, center_unclass)
for x in range(len(original_project)):
    image2display(original_project[x])





