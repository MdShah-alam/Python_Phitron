
class Data:
    def __init__(self) -> None:
        self.data = {
            'order1':{'item': 'laptop' , 'price' : 65000},
            'order2':{'item' : 'tablet' , 'price' : 30000},
            'order3':{'item' : 'watch' , 'price' : 3000},
            'order4':{'item' : 'Phone' , 'price' : 25000},
        }
        
    def get_order_datail(self,orderId):
        return self.data[orderId]
    
class Application:
    pass

class GUI:
    pass

