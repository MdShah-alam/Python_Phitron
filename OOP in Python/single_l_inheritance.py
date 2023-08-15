#sengle level inheritance

# base/parent class

class Device:
    def __init__(self,brand,price,color) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        
        
class Laptop(Device):
    def __init__(self,brand,price,color,dics) -> None:
        super().__init__(brand,price,color)
        self.size_dics=dics
        
    def run(self):
        print('This laptop run well')
        
    def __repr__(self) -> str:
        return f'Laptop {self.brand} : {self.price} : {self.color}'
        
    def purchese(self,money,discount):
        if money>=(self.price-self.price*discount/100):
            print('This laptop for you')
            return money-self.price
        else:
            return f'This laptop is not for you'
               
        
class Phone:
    def __init__(self,brand,price,color,camera,sim_num) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.camera=camera
        self.sim_num=sim_num
        
    def dual_sim(self):
        return self.sim_num>1
    
    def __repr__(self) -> str:
        return f'Phone {self.brand} : {self.price} : {self.color}'
    
    def purchese(self,money,discount):
        if money>=(self.price-self.price*discount/100):
            print('This laptop for you')
            return money-self.price
        else:
            return f'This laptop is not for you'
          
        
class Watch:
    def __init__(self,brand,price,color,watch_type) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.watch_type=watch_type
        
        
    def is_digital(self):
        return self.watch_type=='digital'
    
    def purchese(self,money,discount):
        if money>=(self.price-self.price*discount/100):
            print('This laptop for you')
            return money-self.price
        else:
            return f'This laptop is not for you'
    
    
class Manager:
    def __init__(self,name,salary,experience,designation) -> None:
        self.name=name
        self.salary=salary
        self.experience=experience
        self.designation=designation
        
    def deposite(self,money):
        pass
    
    def widthdraw(self,money):
        pass
    
class Salesman:
    def __init__(self,name,salary,experience,designation,comission) -> None:
        self.name=name
        self.salary=salary
        self.experience=experience
        self.designation=designation
        self.comission=comission
        
    def deposite(self,money):
        pass
    
    def widthdraw(self,money):
        pass     
      
      
hp=Laptop('HP',52000,'silver','500gb')
lenovo=Laptop('Lenovo',42000,'black','256gb')
# print(hp)
# print(lenovo)

ridme=Phone('xaomi',25000,'black','15mp',2)
samsung=Phone('samSung',23000,'silver','12mp',1)

# print(ridme)
# print(samsung)
# print(ridme.dual_sim())
# print(samsung.dual_sim())
print(hp.brand)


        