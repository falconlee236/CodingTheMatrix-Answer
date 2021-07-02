from eigenfaces import load_images
from vec import Vec


# Task 12.6.1
faces_img = load_images("../img/faces")
D = [(x, y) for x in range(166) for y in range(189)]
faces_vec = {key: Vec(set(D), {x: value[x[1]][x[0]] for x in D}) for key, value in faces_img.items()}
print(len(faces_vec))