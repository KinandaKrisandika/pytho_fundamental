import numpy as np

a = [1,2,3,4,5]
b = np.array([1,2,3,4,5])
c = np.array([6,7,8,9,10])

# print(a)
# print(b)
# print(c)

# The different is

a = a + [1] # if we're not use numpy, its just add 1 to end of the list 
b = b + 1  # if we use numpy, it's will be sum 1 by 1 on the list

# Aritmatika
d = b * c 
e = b**2
f = c / b
g = np.arange(10)**2

# print(a)
# print(b)
# print(g)

ab = np.arange(2,12,2)
print(ab)