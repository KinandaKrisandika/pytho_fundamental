def convert_temperature(degrees,from_unit,to_unit):
    c_to_f = 5/9*(degrees-32)
    k_to_f = 5/9*(degrees-32)+273
    
    f_to_c = ((9/5)*degrees)+32
    k_to_c = degrees+273
    
    c_to_k = degrees - 273
    f_to_k = 9/5*(degrees-273)+32
    
    
    if from_unit == "f":
        if to_unit == "c":
            print(f"{degrees} F = {f_to_c} C")
        elif to_unit == "k":
            print(f"{degrees} F = {f_to_k} Kelvin\n")
            
    if from_unit == "c":
        if to_unit == "f":
            print(f"{degrees} C = {c_to_f} F")
        elif to_unit == "k":
            print(f"{degrees} C = {c_to_k} Kelvin\n")
        
    if from_unit == "k":
        if to_unit == "f":
            print(f"{degrees} Kelvin = {k_to_f} C")
        elif to_unit == "c":
            print(f"{degrees} Kelvin = {k_to_c} C")

    
convert_temperature(10,"k","f")