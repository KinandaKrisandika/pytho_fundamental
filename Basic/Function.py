# def example():
#     #print on this example is a body of function
#     print("This is for example")
#     print("nothing special here")
#     print("example just for example")
    
# example()

#example function with argument

# def example(Selling,investment):
#     Total = Selling + investment
#     print(f"{Selling} + {investment} = {Total}")

# example(10,200)

# def name(to="kinanda", frm="sidiq"):
#     print(f'Hello {to}, My Friend I am {frm}')
# name(krisandika)

# def Find_average():
#     list = [2,4,6,8]
#     average = sum(list) / len(list)
#     print(f"Average of list is : {int(average)}\n")

# Find_average()


def reverse_name(name):
    list_name = list(name)
    list_name.reverse()
    hasil = ""
    for i in list_name :
        hasil += i   
    print(f'My name is :{name}')
    print(f'The reverse of name is :{hasil}\n')
    

reverse_name("Kinanda")


# def temperature(celcius, fahrenheit):
#     Hasil = ((fahrenheit)*celcius)+32
#     print("Converter Celcius to Fahrenheit")
#     print(f'{celcius}C = {Hasil}F')
    

# temperature(1,9/5)


# def temp(degrees,celcius,fahrenheit):
#     F = 5/9*(degrees-32)
#     C = ((9/5)*degrees)+32
#     if F == -12.222222222222223:
#         print(f"{degrees}F = {F} C")
#     elif C == 50:
#         print(f"{degrees}C = {C} F")
    
# temp(10,12,13)