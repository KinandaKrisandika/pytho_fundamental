class onepiece:
    list = []
    # Static variable / variable of class
    def __init__ (self,inputname,inputhealth):
        # Instance variable
        self.name = inputname
        self.health = inputhealth
        onepiece.list.append(inputname)
    
    # void function / method tanpa return
    def who(self):
        print("My name is " + self.name)
        
    # method with argument
    def healthup(self,up):
        self.health += up
    
    # method with return
    def gethealth(self):
        return self.health
        
hero1 = onepiece("zoro",100)
hero2 = onepiece("sanji",100)

print(onepiece.list)
print(hero1.name)

hero2.who()
hero1.healthup(10)

print(hero1.__dict__)
print(hero1.gethealth())