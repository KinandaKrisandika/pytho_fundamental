import pandas as pd

data = {
        'Nama' : ['Kinanda','Sidik','Edward','Sandiego','Luffy',"Nami","Robin",
                  'Putra',"Sutikno","Putri","kodrat","Jhonny","Angelica",
                  "Rico","Muslim","Santos","Dulay","Benet","Akew","Beler"],
        'Usia' : [18,20,16,25,29,19,30,28,26,23,25,24,32,40,18,19,27,31,
                  28,35],
        'Kota' : ['Cimahi','Bandung','Karawang', 'Bogor','Jakarta','Depok',
                  'Bekasi','Tangerang','Tasikmalaya','Garut','Sukabumi',
                  'Sumedang','Banten','Cimahi','Bogor','Bandung','Tangerang',
                  'Sumenep','Jakarta','Cimahi']
        }

data = pd.DataFrame(data) # untuk membuat sebuah dataframe
print(data.head()) #Untuk meunjukan 5 teratas dari data

data.to_csv('task_pandas_kinanda.csv', index=False) #utuk megexport file ke csv / menyimpan file dalam bentuk csv

# NOTE !!!
# index = False berfungsi untuk tidak menyertai index di dalam csv