import pandas as pd

data_update = pd.read_csv('update_data.csv')

top5 = data_update.head()
print(f"top 5 dari data frame adalah : \n{top5}") # untuk menyaring 5 teratas dari dataframe

selected_data = data_update.query ('Usia > 25')
print (f"\nUsia yang lebih dari 25 tahun adalah sebagai berikut : \n{selected_data}") # untuk menyaring data usia yang lebih dari 25 tahun

selected_2data = data_update [(data_update ['Usia'] > 30) & (data_update ['Gender'] == 'P')]
print(f"\ncari perempuan yang usia nya lebih dari 30 th di data frame :\n{selected_2data}") # Memakai & untuk memilih kedua item apabila kedua nya True maka akan di tampilkan

print(f"\nakses data ke 3 dari dataframe \n{data_update.loc[3]}") #untuk indexing
print(f"\nakses data ke 4 dari dataframe \n{data_update.loc[4]}\n")

average_age = sum(data_update['Usia']) / len(data_update['Usia']) 
print(f"average age of dataframe is : {average_age}") # untuk mencari rata rata usia pada datafrane