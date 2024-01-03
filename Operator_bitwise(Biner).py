a = 9
b = 2

#Example for OR
c = a|b
print("\n====OR====")
print('\nValue a:',a,' on binary is:', format(a, '08b'))
print('\nValue b:',b,' on binary is:', format(b, '08b'))
print('---------------------------------------( | )')
print('Value c:',c,' on binary is:', format(c, '08b'))

#Example for AND
c = a&b
print("\n====AND====")
print('\nValue a:',a,' on binary is:', format(a, '08b'))
print('\nValue b:',b,' on binary is:', format(b, '08b'))
print('---------------------------------------( & )')
print('Value c:',c,' on binary is:', format(c, '08b'))

#Example for XOR
c = a^b
print("\n====XOR====")
print('\nValue a:',a,' on binary is:', format(a, '08b'))
print('\nValue b:',b,' on binary is:', format(b, '08b'))
print('---------------------------------------( ^ )')
print('Value c:',c,' on binary is:', format(c, '08b'))

# Example for flip NOT
c = ~ b
print("\n====NOT====")
print('\nValue b:',b,' on binary is:', format(b, '08b'))
print('---------------------------------------( ~ )')
print('Value c:',c,' on binary is:', format(c & 0xFF, '08b'))

# Example for Shifting

# Shifting Right
c= a >> 2
print("\n====Shift Right====")
print('\nValue a:',a,' on binary is:', format(a, '08b'))
print('---------------------------------------( >> )')
print('Value c:',c,' on binary is:', format(c, '08b'))

# Shifting Left
c= a << 2
print("\n====Shift Left====")
print('\nValue a:',a,' on binary is:', format(a, '08b'))
print('---------------------------------------( << )')
print('Value c:',c,' on binary is:', format(c, '08b'))