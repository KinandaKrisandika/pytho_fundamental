import numpy as np

# Task 1 membuat bilangan acak dari 1 - 10
a = np.arange(2,11)
# print(a)

# Task 2 Menghitung jumlah rata2 dari array yang telah di buat
b1 = sum(a)
b2 = len(a)
b = sum(a) / len (a)
# print(b1)
# print(b2)
# print(int(b))

# Task 3 membuat 2 buah bilangan matrix
c1 = np.array ([(12,22,32) , (42,52,62), (72,82,92)])
c2 = np.array ([(2,4,6) , (8,10,12), (14,16,18)])
# print(c1)

# Task 4 operasi Aritmatika Element wise operation
d1 = c1 + c2
print(d1)

d2 = c1 - c2
# print(d2)

d3 = c1 * c2
# print(d3)

d4 = c1 / c2
# print(d4)

d5 = np.dot(c1,c2)
d6 = c1.dot(c2)
# print(d6)
#penjelasan .dot untuk perkalian matrix, pekalian nya bisa pake yang d1, bisa pake yang d2

# Task 5 determinan
e = np.linalg.det(c2)
# print(e)

# Task 6
f = np.array([1,2,3,4,5,6,7,8,9,10])
# print(f)

# Task 7 & Task 8
g = np.arange(2,11,2)
# print(g)

# Task 9
h = np.array([(22,24,26,28),(21,23,25,27),(12,10,14,16),(11,13,15,17)])
h1 = [1,2,3,4,5]
# print(h)

# Task 10
#Average
i = np.mean(h)
# print(i)

#Standard Deviation
i1 = np.std(h)
# print(i1)

i2 = np.median(h)
# print(i2)

# Korelasi
i3 = np.corrcoef(h)
# print(i3)

# Task 11 nilai-nilai dari 0 hingga π dengan interval 0.1
j = np.arange(0,3.14,0.1)
# print(j)

# Task 12 sin cos tan
k = np.sin(j)
print(k)
k1 = np.cos(j)
# print(k1)
k2 = np.tan(j)
# print(k2)

# Task 13 Menghitung minimal maximal dari sin
l = np.max(k)
print(l)
l1 = np.min(k)
print(l1)