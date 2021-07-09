from cancer_data import read_training_data
from matutil import rowdict2mat
from vec import Vec


subfeatures = {'area(worst)', 'smoothness(worst)', 'texture(mean)'}
A, b = read_training_data("../src/data/train.data", subfeatures)
# Task 14.13.1


def main_constraint(i, a_i, d_i, features):
    return Vec({"gamma", "ID"} | features, {})









































