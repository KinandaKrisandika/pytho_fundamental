import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Mengubah bentuk array menjadi (3, 2)
print(arr.reshape(3, 2))


# Mengubah bentuk array menjadi (3, 2)
arr.resize(3, 2)

print(arr)