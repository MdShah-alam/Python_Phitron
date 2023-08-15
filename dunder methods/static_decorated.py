
class Shopping:
    def __init__(self,customer):
        self.customer=customer
        self.item=[]
        self.total=0
        
    @staticmethod
    def multiply(x,y):
        return x*y
    
    def add_to_total(self,amount):
        self.total+=amount
        
    def add_to_crat(self,item,price,quantity):
        item_total=price*quantity
        self.add_to_total(item_total)
        self.item.append(item)
    
    def checkout(self):
        pass
    
result=Shopping.multiply(45,5)
print(result)

my_shopping=Shopping('roni')
my_shopping.add_to_total(450)
my_shopping.add_to_total(450)
print(my_shopping.total)
result_2=Shopping.multiply(30,5)
print(result_2)