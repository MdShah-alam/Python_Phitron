from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    @property
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print('moving around the zoo')

class Monkey(Animal):
    def __init__(self) -> None:
        self.__name='Monkey'
        
    def sing(self):
        print('monkey is signing')
    
    # as a getter
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name=value
    def eat(self):
        print('eating banan')
        
    def move(self):
        print('hanging on the branches of tree')
        super().move()
        
class Tiger(Animal):
    def eat(self):
        pass
    
    def move(self):
        pass
        
layka=Monkey()
print(layka)        
layka.eat()
layka.move()
layka.name='moonkey'
print(layka.name)
# print(layka.name())
