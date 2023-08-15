
class Item:
    all=[]
    def __init__(self,item_name,item_price) -> None:
        self.__item_name=item_name
        self.__item_price=item_price
        self.all.append(self)
        
    def __repr__(self) -> str:
        return f'Item :({self.item_name}, {self.item_price})'
    
item1=Item('Bowl',100)
item2=Item('Plate',150)
item1._Item__discount=10
# item1.__discount=10
print(item1._Item__discount)
print(item1._Item__item_name)
print(item1._Item__item_price)
print(item1.__dict__)
        