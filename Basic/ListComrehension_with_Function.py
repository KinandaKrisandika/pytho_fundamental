def even_square_numbers(n):
    for i in range(2,n,2):
        data = i**2
        print(data)

even_square_numbers(21)

def even_square_numbers(n):
    list_com = [] #This is for list comprehension, where the looping goes into the list
    for i in range(2,n,2): # range (2,n,2) it's mean : start from 2 to n, and we just take the even (2) numbers
        list_com.append(i**2) # append on list.com to add looping of square on looping
    print(list_com)

even_square_numbers(21)

# or we can run code with this one :
def compre(m):
    list_exp = [i **2 for i in range(2,m,2)]
    # it's mean same as above, but it's a simple code, we're code directly on the list comprehension
    print(list_exp)
    
compre(21)