# class Rectangle:
#     def __init__(self, height:int, base:int):
#         self.height = height
#         self.base = base

#     def calculated_area(self):
#         area = self.height * self.base / 2
#         return area


# class Circle:
#     def __init__(self, radius:int):
#         self.radius = radius

#     def calculated_area(self):
#         area = self.radius * 3.14
#         return area

# if __name__ == "__main__":
#     segitiga = Rectangle(10,5)
#     lingkaran = Circle(14)

#     print(segitiga.calculated_area())
#     print(lingkaran.calculated_area())
    
class Person :
    nama : str
    age : int

    def __init__(self, nama, age):
        self.nama = nama
        self.age = age
        self._status = "pelajar" ## contoh encapsulation privat


    def rubah_status (self): ## contoh merubah field encapsulation
        self._status = "mahasiswa"
        return f'{self.nama} sekarang berstatus {self._status}'


    def siswa (self):
        return f'{self.nama} berumur {self.age} tahun dan berstatus {self._status}'

per1 = Person ("joni", 18)

print (per1.siswa()) # cetak hasil awal field privat
print (per1.rubah_status()) # cetak hasil yang sudah merubah field privat

# class Person:
#     nama : str
#     sudah_lulus : bool
#     nilai_ujian : float

#     def __init__(self,nama,sudah_lulus,nilai_ujian):
#         self.__nama = nama
#         self.__sudah_lulus = sudah_lulus
#         self.__nilai_ujian = nilai_ujian
#         #menggunakan underscore 2x untuk mem-private
    
#     # ini getter untuk mengambil data dari variabel yang di privat
#     def getinfo(self):
#         print(f'Nama\t\t: {self.__nama}\nSudah Lulus\t: {self.__sudah_lulus}\nNilai\t\t: {self.__nilai_ujian}')
    
#     # ini setter untuk men set (merubah) variable yang di private
#     def remedial(self,nilai_remedial):
#         self.__nilai_ujian = (self.__nilai_ujian + nilai_remedial) / 2
#         if self.__nilai_ujian >= 7.0:
#             self.__sudah_lulus = True
#         else:
#             self.__sudah_lulus = False
#         print(f'\nSETELAH REMEDIAL\nNama\t\t: {self.__nama}\nSudah Lulus\t: {self.__sudah_lulus}\nNilai\t\t: {self.__nilai_ujian}')
        

# person1 = Person("Firman", False, 6.0)
# person1.getinfo() # output --> mengambil data dari variable yang di private
# person1.remedial(8.9) # output --> mengubah data dari variable yang di private