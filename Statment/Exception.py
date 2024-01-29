future_dreams = 1000
income = 0
try:
    my_result = future_dreams/income
    print(f"The result is {my_result}")
except ZeroDivisionError as a: # we can use this for eror because 0 result
    print(f"Illegal operation (ZeroDivisionEror block) -> {a}")
# except Exception as a: # we can use this for general eror
#     print(f"Illegal operation -> {a}")
    
# NOTE !!!
# metode ini menjelaskan kenapa kode eror
# Ini bisa terjadi karna oprasi yang ilegal atau kode tidak memiliki sebuah hasil / hasil nya 0 atau tidak terdefinisi
# kita dapat menggunakan exception untuk jawaban eror secara umum
# Tapi jika kita ingin jawaban spesifik karna hasil nya 0, kita dapat menggunakan ZeroDivisionEror 
# as untuk alias, untuk memudahkan code setelah nya agar tidak terlalu panjang