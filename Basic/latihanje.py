a = [1,2,3,4]
b = [2,3,4,5]

for i in a :
    if i in b:
        print(i)

c = {20,30,40,50}
d = {20,40,50,80}

# c.intersection(d)
# print(c)

c.remove(40)
print(c)