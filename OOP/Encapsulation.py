class Person :
    def __init__(self,nama,status):
        self.nama = nama
        self.__status = status

    @property
    def status(self):
        pass
    
    @status.getter
    def status(self):
        if self.__status == "Lajang" :
            return f"Tahun 2090 {self.nama} berstatus {self.__status}\n"
        else :
            return f"Setelah banyak kondangan, dan selalu ditanya kapan nikah, besok nya {self.nama} {self.__status}\n"
        
    @status.setter
    def status(self,set):
        self.__status = set
        
        
people = Person("Kinanda","Lajang")

print(people.status) # Tidak memakai () karna sudah di rubah menjadi variable
people.status = "Menikah" #bisa melakukan ini karna setter sudah di anggap sebagai variable
print(people.status)
print(people.__dict__) #untuk melihat apakah data nya sudah berubah apa belum

#Penjelasan
# __status untuk merubah data menjadi private
# @property, untuk merubah sebuah method menjadi variable
# menggunakan self.__status untuk mengambil data yang sudah di private, di sebut juga denga getter
# Apabila ingin mengupdate data private kita menggunakan setter