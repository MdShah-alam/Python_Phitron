
class GroupChat:
    def __init__(self) -> None:
        self.__observers=[]
        
    def attach(self, observer):
        self.__observers.append(observer)
        
    def add_new_message(self,msg):
        self.notify(msg)
        
    def notify(self, msg):
        for observer in self.__observers:
            observer.updata(msg)
            
class Observer:
    def __init__(self , name) -> None:
        self.name=name
        
    def updata(self,msg):
        print(f'New Message for {self.name} : {msg} .')
        
messanger = GroupChat()

abid = Observer('Abide')
navid = Observer('Navide')
sabid = Observer('sabid')

messanger.attach(abid)
messanger.attach(navid)
messanger.attach(sabid)

messanger.add_new_message('hey bor or sis')
