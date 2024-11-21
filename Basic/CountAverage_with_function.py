data = [2,4,6,8]

def find_average(amount): 
    average = sum(amount) / len(amount)
    print(f"Average of list is : {int(average)}")

find_average(data)

# pejelasan :
# find_average adalah nama function, (amount adalah sebagai parameter nya)
# di dalem variable average ada sum untuk penjumlahan, dan ada len untuk menghitung jumlah ada berapa data yang ada pada list
# di dalam print ada pemakaian data casting, di sini pake int biar hasil nya ga jadi float
# variable data ada di luar function, yang nanti nya di panggil oleh function find_average untuk di jadikan sebuah parameter
# notes : variable data di taro di atas cuma buat contoh aja, jadi bisa di taro di mana aja di luar fungsi