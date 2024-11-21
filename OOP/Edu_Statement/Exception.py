# future_dreams = 1000
# income = 0
# try:
#     my_result = future_dreams/income
#     print(f"The result is {my_result}")
# except ZeroDivisionError as a: # we can use this for eror because 0 result
#     print(f"Illegal operation (ZeroDivisionEror block) -> {a}")
# except Exception as a: # we can use this for general eror
#     print(f"Illegal operation -> {a}")
    
# NOTE !!!
# metode ini menjelaskan kenapa kode eror
# Ini bisa terjadi karna oprasi yang ilegal atau kode tidak memiliki sebuah hasil / hasil nya 0 atau tidak terdefinisi
# kita dapat menggunakan exception untuk jawaban eror secara umum
# Tapi jika kita ingin jawaban spesifik karna hasil nya 0, kita dapat menggunakan ZeroDivisionEror 
# as untuk alias, untuk memudahkan code setelah nya agar tidak terlalu panjang

print("\nTahun Kabisat atau bukan")
import datetime
tahun = int(input('masukkan tahun: '))
tgl_awal = datetime.date(tahun,1,1)
tgl_akhir = datetime.date(tahun + 1,1,1)
jml_hari = (tgl_akhir - tgl_awal).days
if jml_hari == 366:
    print(f'tahun {tahun} terdapat {jml_hari} hari')
    print(f'tahun {tahun} adalah tahun kabisat')
else:
    print(f'tahun {tahun} terdapat {jml_hari} hari')
    print(f'tahun {tahun} bukan tahun kabisat')

# print("\nAngka ganjil 1 - 50 ")
# print("Coba Pakai list comprehension")
# list = [i for i in range(1,50) if i%2 == 1]
# print(list)
# print("\ncoba tanpa list comprehension")
# a = 0
# list = ""
# while a != 50:
#     a += 1
#     if a%2 == 1:
#         print(list)