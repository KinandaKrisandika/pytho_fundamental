# def count_character(string):
#     amount = {
#        "K" : string.count("K"),
#        "i" : string.count("i"),
#        "n" : string.count("n"),
#        "a" : string.count("a"),
#        "d" : string.count("d")
#     }
#     print(f"The counts of every characters in {string} =")
#     for slepet,gemoy in amount.items() :
#         print(f"{slepet} : {gemoy}")


# count_character("Kinanda")

# def count_character(name):
#     list_name = list(name)
#     # amount = {
#     #    "".count("K"),
#     #    "".count("i"),
#     #    "".count("n"),
#     #    "".count("a"),
#     #    "".count("n"),
#     #    "".count("d"),
#     #    "".count("a")
#     # }
#     # result = ""
#     for looping in list_name : 
#         # result += looping 
#     print(f'My name is :{name}')
#     print(f"The reverse of name is :{looping}\n")
    
# count_character("Kinanda")

def count_character(name):
    list_name = list(name)
    amount = {
       "".count("K"),
       "".count("i"),
       "".count("n"),
       "".count("a"),
       "".count("n"),
       "".count("d"),
       "".count("a")
        
    }
    for looping in list_name:
        print(looping.count(amount))

count_character("Kinanda")