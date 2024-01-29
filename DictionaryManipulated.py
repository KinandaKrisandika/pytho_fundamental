def count_character(name):
    list_character = list(name)
    amount = dict()

    for keys in list_character :
        # amount[keys] = list_character.count(keys) 
        amount.update({keys:list_character.count(keys)}) # The result is same
        
    print(amount)

count_character("Kinanda")

# NOTE !!!
# kalo key nya sama maka dia akan mengupdate value nya
# tapi kalo key nya beda, maka dia akan menambahkan data baru kedalam dictionary

# IN ENGLISH !
# if teh key is same, its just to be update the value
# but if the key is different from dictionary, so it will be add new data into dictionary