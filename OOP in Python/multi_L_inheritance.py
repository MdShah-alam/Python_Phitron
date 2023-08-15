

class Vehicle:
    def __init__(self,name,price,lisence) -> None:
        self.name=name
        self.price=price
        self.lisence=lisence
        print('Vehicle is called')
        
    def start(self):
        print(f'{self.name} is started')
        
class Bus(Vehicle):
    def __init__(self, name, price, lisence,seat,ticket_price) -> None:
        super().__init__(name, price, lisence)
        self.seat=seat
        print('Bus init called')
        self.avialableseat=seat
        self.ticket_price=ticket_price
        
    def purchese_ticket(self,customer_name, quantity,amount):
        self.avialableseat-=quantity
        remainder=amount-quantity*self.ticket_price
        if remainder>=0:
            return Ticket(customer_name)
        else:
            return f'insufficient balance {amount}'
        
class ACBus(Bus):
    def __init__(self):
        print('AC bus created')
    
class MiniBus(Bus):
    def __init__(self):
        print('Mini bus created')
        super().__init__('MiniBus',1200000,'123AM',20,200)
       
        
class Ticket:
    def __init__(self,ower) -> None:
        self.ower=ower
   
mini=MiniBus()
# print(mini)
print(mini.name)
print(mini.seat)
        