# poly=many
# morph=different

# print(4+6)
# print('Hello'+'Bondhu')
# print([43,65,32]+[12,34,32])

# overriding function is make_sound()

class Animal:
    def __init__(self,name) -> None:
        self.name=name
        
    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def make_sound(self):
        print('meow meow meow')

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        
    def make_sound(self):
        print('bark bark bark')
        
class Horse(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def make_sound(self):
        print('ney ney ney')
        
            
don=Cat('don')
# don.make_sound()

dog=Dog('Shepard')
# dog.make_sound()

manik=Horse('manik roton')
# manik.make_sound()

don2=Dog('Asol don')

animals=[don,dog,manik,don2]

for animal in animals:
    animal.make_sound()
      
