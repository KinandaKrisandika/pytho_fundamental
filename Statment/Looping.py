print("Menampilkan angka ganjil dari 1 - 50\n")

list = []

for i in range (50):
    if i%2 != 0:
        list.append(i)
        print(f"Diantaranya : {i}")
        
print(f"\nJumlah angka ganjil antara 1-50 ada : {len(list)} angka")
        