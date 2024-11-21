number : int = 12
number_2 : float = 30.5
boolean_var = True
string_var = "My string"

StudentDb = {
    "01" : {
        "Name" : "Slepet",
        "Age" : 12,
        "Hobby" : ["Public Speaking","upgrade sarung to the next level"]
    },
    "02" : {
        "Name" : "Gemoy",
        "Age" : 12,
        "Hobby" : ["dancing","Ready For War"]
    }
}


if __name__ == '__main__':
    # print(number + number_2)
    # print(number + boolean_var)
    # print(number + string_var)
    # number = float (number)
    # print(number, type(number))
    print(StudentDb ["02"])