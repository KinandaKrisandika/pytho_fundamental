class Vehicle:
    def __init__(self,jenis,merk):
        self.jenis = jenis
        self.merk = merk
    
    def info(self):
        print("Saya memiliki {} dengan merk {}".format(self.jenis,self.merk))
    
class Car(Vehicle):
    def __init__(self,jenis):
        super().__init__(jenis,"chefrolex")
        super().info()

class Bicycle(Vehicle):
    def __init__(self,jenis):
        super().__init__(jenis,"polygong")
        super().info()

mobil = Car("mobil")
Sapedah = Bicycle("sapedah")


#Penjelasan
#Vehicle sebagai class utama
#Car dan bicycle adalah sebagai inheritance nya vehicle
#di tandai dengan memasukan (vehicle) ke setiap class
#method super() adalah metode untuk mewarisi class utama
#super().info() untuk memanggil info yang ada di class utama