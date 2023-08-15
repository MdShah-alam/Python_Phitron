

class Phone:
    
    manufactured='china'
    
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
        
    def send_sms(self,number,text):
        sms=f'sending : {text} to :{number} .'
        return sms
    
my_phone=Phone('Oppo',25000,'blue')
print(my_phone.brand , my_phone.manufactured)

her_phone=Phone('iphone',90000,'purple')
print(her_phone.brand, her_phone.manufactured)

dad_phone=Phone('Nokia',5000,'black')
print(my_phone.brand,her_phone.brand,dad_phone.brand)