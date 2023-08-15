
class Shopper:
    def __init__(self,name):
        self.name=name
        self.cart=[]
        
    def add_to_cart(self, item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})
        
    def checkout(self,amount):
        price=0
        for item in self.cart:
            print(item)
            price+=item['price']*item['quantity']
        print(price)
        
shopping=Shopper('shi jing ping')
shopping.add_to_cart('shirt',400,3)
shopping.add_to_cart('shoes',5000,2)
shopping.add_to_cart('pant',2000,3)

shopping.checkout(50000)