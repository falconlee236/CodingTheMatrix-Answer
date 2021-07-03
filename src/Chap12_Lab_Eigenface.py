from eigenfaces import load_images, test_M, test_x
from image import image2display
from matutil import rowdict2mat, mat2coldict, coldict2mat
from svd import factor
from vec import Vec
import copy


# Task 12.6.1
faces_img = load_images("../img/faces")


# Task 12.6.2
def make_centeringVec(imgdict):
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
    centering_img = copy.deepcopy(imgdict)
    for img in centering_img.keys():
        for i in range(189):
            for j in range(166):
                centering_img[img][i][j] -= center[i][j]
    return centering_img


center_img = make_centeringVec(faces_img)


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


print(projected_representation(test_x, test_M))































