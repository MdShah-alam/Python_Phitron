
class Bike:
    def __init__(self,driver,rate):
        self.name=driver
        self.rate=rate
        
    def get_fare(self,distance):
        return distance * self.rate
    
class Car:
    def __init__(self,driver,rate) -> None:
        self.name=driver
        self.rate=rate
        
    def get_fare(self,distance):
        return distance*self.rate
    
class CNG:
    def __init__(self,driver,rate) -> None:
        self.name=driver
        self.rate=rate
        
    def get_fare(self,distance):
        return distance * self.rate
    
b1=Bike('masud',10)
c1=Car('mahhabub',25)
g1=CNG('karim',15)
print(b1.get_fare(20))
print(c1.get_fare(20))
print(g1.get_fare(20))