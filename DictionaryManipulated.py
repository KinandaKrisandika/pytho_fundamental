def count_character(name):
    list_character = list(name)
    amount = dict()

    for keys in list_character :
        amount[keys] = list_character.count(keys)
        
    print(amount)

count_character("Kinanda")