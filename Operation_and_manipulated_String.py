first_name = "Kinan"
middle_name = "D'"
last_name = "Krisandika"
full_name = first_name + " " + middle_name + " " + last_name

print(full_name)

# Count Length of string
Length = len(full_name)
print(Length, type(Length))

# Check a component is exist or not on the sting
status = "D" in full_name
print('\nis "D" exist on the string ?', status, type(status))

# Create a same component with multiple
print("=="*4)

# How to check some component with []
print("index for -0 = ", full_name[0])
print("index for [0:5] = ", full_name[0:6])
print("index for [0,2,4,5,6,8,10] = ", full_name[0:13:2])

# How to check max/min grade of string
print("The Biggest is = ", max(full_name))
print("The Lowest is = ", min(full_name))

# How to count some component on the string
Amount = full_name.count("a")
print(f"Amount of \"a\" on the {full_name} is {Amount}")

# How to Uppercase/ Lowercase
print("Create Upper for : ", full_name.upper())

# Merging compponent with join() ad split()
Title = ["Arakawa","Under", "Bridge"]
Merging = ' '.join(Title)
print(Title)
print(Merging)
deleted = Merging.split(" ")
print(deleted)

# Allocation character rjust(), ljust(), center()
Center = "Koe no Katachi".center(20,"*")
print(Center)

# The Opposite is strip()
Center = Center.strip("*")
print(Center)

Name = "Kinanda"
print(Name)
Name = list(Name)
Name.reverse()
print("".join(Name))