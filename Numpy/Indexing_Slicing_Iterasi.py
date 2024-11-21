import numpy as np

a = np.arange(10)**2
print(a)

#Indexing
print("mengambil data pertama", a[0])
print("megambil data terakhir", a[-1])

#Slicing
print("mengambil data 1-6",a[0:6])
print("mengambil data dari elemen ke 4 sampai akhir",a[3:])
print("mengambil data dari awal sampai 5", a[:5])

#iterasi
for i in a:
    print("Nilai dari a : ",i)