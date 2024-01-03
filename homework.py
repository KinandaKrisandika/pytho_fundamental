print("Comparasion with Logic\n")
# ---0++++5----8++++11----
Number = int(input("Input number more than 0,\nless than 5,\nmore than 8,\nand less than 11 " ))

# Number more than 0
Ismorethanzero = Number > 0
print("More than 0 =", Ismorethanzero)

# Number less than 5
Islessthanfive = Number < 5
print("Less than 5 =", Islessthanfive)

# Number more than 8
Ismorethaneight = Number > 8
print("More than 8 =", Ismorethaneight)

# Number less than 11
Islessthaneleven = Number < 11
print("Less than 11 =", Islessthaneleven)

# Ismorethanzero or Islessthanfive and Ismorethaneight or Islessthaneleven
Iscorrect = Ismorethanzero and Islessthanfive or Ismorethaneight and Islessthaneleven
print ("Your input number =", Iscorrect)