class people:
    RACE = "HUMAN"
    CLASS = "MAMALIA"
    
    def __init__(self,name:str):
        self.name = name
        self.level = "reguler" #Encapsulation
        
    def greet(self):
        print(f"Hello my name is {self.name}")
        
    def set_level(self,level:str):
        self._level = level
        
    def get_level(self):
        print(f"{self.name}'s path is {self._level}")
        
    def is_adult(age:int) -> bool:
        return age > 20
        
    @classmethod
    def set_race(cls,race:str): #Abstraction
        print("Previous race :", cls.RACE)
        cls.RACE = race
        print("After race :", cls.RACE)
        
people1 = people("Amir")

print(people1.__dict__)