def reverse_name(name):
    list_name = list(name) # Change a name to be a list
    list_name.reverse() # reverse name after name converted into a list
    result = "" # String blank it's just for the result of looping
    for looping in list_name : # it is for looping the name on the list
        result += looping # and the loops are entered one by one into the result
    print(f'My name is :{name}')
    print(f'The name after being converted into a list and reversed :{list_name}')
    print(f'The reverse of name is :{result}\n') # After looping, and entered to the string on the result variable
    
reverse_name("Kinanda")

# This condition is just for example, if we're not put variable result into looping
list_name = list("Kinanda")
list_name.reverse()
for looping in list_name :
    print(looping)

