class onepiece:
    list = []
    # Static variable / variable of class
    def __init__ (self,inputname,inputhealth):
        # Instance variable
        self.name = inputname
        self.health = inputhealth
        onepiece.list.append(inputname)
        
hero1 = onepiece("zoro",100)
hero2 = onepiece("sanji",100)

print(onepiece.list)
print(hero1.name)
print(hero1.__dict__)

# NOTE !!!
# Init for initialitation
# variable hero1 & hero2 as a self


    
    