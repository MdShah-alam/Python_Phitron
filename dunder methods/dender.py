
class Persion:
    
    def __init__(self,name,age,money,height=65) -> None:
        self.name=name
        self.age=age
        self.money=money
        self.height=height
        
    def __add__(self,other):
        # return self.money+other.money
        # return self.name+other.name
        return self.age+other.age
    
    def __call__(self):
        print(f'This is {self.name} with age {self.age} and have {self.money} .')
        
    
    def __eq__(self,other):
        return self.money==other.money
    
    def __len__(self):
        return self.height
        
        
alim=Persion('alim',15,500,76)
dalim=Persion('Dalim',16,700)
print(alim+dalim)
alim()
print('compare two objects : ', alim==dalim)

print(len(alim))        