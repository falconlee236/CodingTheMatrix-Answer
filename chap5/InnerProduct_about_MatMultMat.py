import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module.matutil import coldict2mat
from module.mat import Mat
from module.vec import Vec

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
print(M)
