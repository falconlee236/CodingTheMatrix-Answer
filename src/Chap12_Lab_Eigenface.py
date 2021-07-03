from eigenfaces import load_images
from image import image2display
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
