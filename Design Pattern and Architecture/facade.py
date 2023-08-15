
class Washing:
    '''Subsystem # 1'''
 
    def wash(self):
        print("Washing...")
 
 
class Rinsing:
    '''Subsystem # 2'''
 
    def rinse(self):
        print("Rinsing...")
 
 
class Spinning:
    '''Subsystem # 3'''
 
    def spin(self):
        print("Spinning...")
        
class Dryer:
    ''' Subsystems # 4'''
    
    def dry(self):
        print('Drying your clothes')
        
class Ironer:
    ''' Subsystem # 5'''
    
    def iron(self):
        print('Ironing your address')
 
 
class WashingMachine:
    '''Facade'''
 
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
        self.drying= Dryer()
        self.ironing = Ironer()
 
    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
        self.drying.dry()
        self.ironing.iron()
        
philips=WashingMachine()
philips.startWashing()