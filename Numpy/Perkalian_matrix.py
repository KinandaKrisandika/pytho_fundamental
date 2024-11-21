import numpy as np

a = np.array([(1,2,3),(4,5,6)])
b = np.ones([3,3])
# print(a)
# print(b)

# c = a * b #perkalian biasa
#perkalian matrix
d = np.dot(a,b)
e = a.dot(b)


print(d)