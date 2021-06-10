import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.vec import Vec


# Task 6.12.1
def move2board(y):
    return Vec(y.D, {key: value / y['y3'] for key, value in y.f.items()})


print(move2board(Vec({'y1', 'y2', 'y3'}, {'y1': 3, 'y2': 7, 'y3': 0.2})))
