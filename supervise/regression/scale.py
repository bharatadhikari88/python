import numpy
from sklearn import preprocessing

data = [[1, 4, 400, 10000, 100000], [1, 4, 400, 10000, 100000]]

ss = preprocessing.StandardScaler()

print(preprocessing.normalize(data)) 
print("scale")
print(preprocessing.scale(data)) 
