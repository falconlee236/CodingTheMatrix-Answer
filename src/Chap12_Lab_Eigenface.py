from eigenfaces import load_images
from image import image2display
from vec import Vec


# Task 12.6.1
faces_img = load_images("../img/faces")
'''
D = [(x, y) for x in range(166) for y in range(189)]
faces_vec = {key: for key, value in faces_img.items()}
faces_vec = {key: Vec(set(D), {x: value[x[1]][x[0]] for x in D}) for key, value in faces_img.items()}
'''


# Task 12.6.2
print(faces_img[0][0])
# image2display(faces_img[0])