
from abc import ABC,abstractmethod
from time import sleep
class Vehicle:
    speed={
        'car' : 30,
       'bike' : 50,
        'cng' : 20
    }
    def __init__(self,vehicle_type,license_plate,rate,driver) -> None:
        self.vehicle_type=vehicle_type
        self.rate=rate
        self.status='available'
        self.driver=driver
        self.license_plate=license_plate
        self.speed=self.speed[vehicle_type]
    
    @abstractmethod  
    def start_driving(self):
        pass
    
    @abstractmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type,license_plate, rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)
        
    def start_driving(self,start,destination):
        self.status='unavailable'
        print(self.vehicle_type, self.license_plate ,'started')
        distance=abs(start-destination)
        for i in range(0,distance):
            # sleep(0.2)
            print(f'Driving :{self.license_plate} current position : {i} of {distance}\n')
        self.trip_finished()
    
    def trip_finish(self):
        self.status='available'
        print(self.vehicle_type, self.license_plate , 'finished')

        
class Bike(Vehicle):
    def __init__(self, vehicle_type,license_plate, rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)
        
    def start_driving(self,start,destination):
        self.status='unavailable'
        print(self.vehicle_type, self.license_plate ,'started')
        distance=abs(start-destination)
        for i in range(0,distance):
            # sleep(0.2)
            print(f'Driving :{self.license_plate} current position : {i} of {distance}\n')
        self.trip_finish
    
    def trip_finish(self):
        self.status='available'
        print(self.vehicle_type, self.license_plate , 'finished')

        
class Cng(Vehicle):
    def __init__(self, vehicle_type,license_plate, rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)
        
    def start_driving(self,start,destination):
        self.status='unavailable'
        print(self.vehicle_type, self.license_plate ,'started')
        distance=abs(start-destination)
        for i in range(0,distance):
            # sleep(0.2)
            print(f'Driving :{self.license_plate} current position : {i} of {distance}\n')
        self.trip_finish
    
    def trip_finish(self):
        self.status='available'
        print(self.vehicle_type, self.license_plate , 'finished')

        