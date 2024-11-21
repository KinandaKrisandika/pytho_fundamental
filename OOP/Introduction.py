class Hero: # This is for templated
    pass


hero1 = Hero() # This is for object
hero2 = Hero()
hero3 = Hero()

hero1.name = "Zoro" # This is an atribute
hero1.health = 100

hero2.name = "Sanji"
hero2.health = 100

hero3.name = "Katakuri"
hero3.health = 100

print(hero1)
print(hero1.__dict__) # we must use 2 underscore for the method
print(hero1.name)
print(Hero)

# NOTE :
# on the templated, we can enter many object
# and object has an atribute