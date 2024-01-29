my_list = [1,2,3,'string',(1,2,3)]

my_map = {
    "key_1": 1,
    "key_2": 2
}

my_map_2 = {
    "key_3": 3,
    "key_4": 4
}

if __name__ == '__main__' :
    # print (my_list[-1])
    # my_list.append(1000)
    # print(my_list)
    # my_map.update(my_map_2)
    del my_map["key_1"] #if u want to delete your data in dictionary, it's just choose the key
    print(my_map)