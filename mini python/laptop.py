
class Laptop:
    def __init__(self,brand,age):
        self.brand=brand
        self.age=age
    
    def inreage_age(self,age=1):
        self.last_age=self.age
        self.age=self.age + age
        
    def repair(self,life_increage=-5):
        self.inreage_age(life_increage)
        
my_laptop.inreage_age()
my_laptop.age=17
my_laptop.inreage_age()
my_laptop.inreage_age()
print(my_laptop.age)
print(my_laptop.last_age)
my_laptop.repair()
print(my_laptop.age)
print(my_laptop.__dict__)