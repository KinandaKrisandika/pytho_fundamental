import numpy as np

# Create a vector
a = np.array([1,2,3,4,5])

# Create a vector with range
b = np.arange(1,10,2)

# Create linspace
c = np.linspace(1,10,3)

# Create array multi dimensi / matrix
d = np.array ([(1,2,3) , (4,5,6)])

# Matrix with zero value
e = np.zeros((5,5))

# Matrix with 1 value
f = np.ones((5,5))

# matrix with identity
g1 = np.identity(5)
g2 = np.eye(5)

print(d)