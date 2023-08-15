import json
class Item:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price     
    def initialize(self):
        with open('extract.txt','r') as file:
            data=file.read()
            js=json.loads(data)
            print(js)         
item=Item('test',50)
item.initialize()
