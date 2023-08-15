
import hashlib
import threading
from brta import BRTA
from random import random ,randint,choice
from vehicle import Cng,Bike,Car

from ride_manager import uber

class UserAlreadyExist(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f'you are access more {email}')
        super().__init__(*args)


license_authority = BRTA()

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        pwd_encrypted=hashlib.md5(password.encode()).hexdigest()
        already_exist=False
        with open('users.txt','r') as file:
            if email in file.read():
                already_exist=True
                # raise UserAlreadyExist(email)
        file.close()
        if already_exist==False:
            with open('users.txt','a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
            file.close()
        # print(self.name, 'user created')
        
    @staticmethod
    def log_in(email,password):
        stored_password=''
        with open('users.txt','a') as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_password=line.split(' ')[1]
        
        file.close()
        hash_password=hashlib.md5(password.encode()).hexdigest()
        if hash_password==stored_password:
            print('valid user')
            return True
        else:
            print('invalid user')
            return False
        # print('password found ',stored_password)     


class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.balance=balance
        self.__trip_history=[]
        
    def set_location(self,location):
        self.location=location
        
    def get_location(self):
        return self.location
    
    def get_trip_history(self):
        return self.__trip_history
    
    def start_trip(self,fare,trip_info):
        print(f'A trip started for {self.name}')
        self.__trip_history.append(trip_info)
        self.balance -= fare
        
class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.__trip_history=[]
        self.license=license
        self.valid_driver= license_authority.valideta_license(email,license)
        self.earning=0
        self.vehicle=None
        
    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result == False:
            # print('sorry you failed , try again ')
            return None
            
        else:
            self.license=result
            self.valid_driver=True
            
    def register_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            self.vehicle = None
            if vehicle_type=='car':
                self.vehicle=Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type=='bike':
                self.vehicle=Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
                
            else:
                self.vehicle=Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
                
        
        else:
            # print('you are not a valid driver')
            pass
        
    def start_trip(self,start,destination,fare,trip_info):
        self.__trip_history.append(trip_info)
        self.earning += fare
        # start thread
        trip_thread=threading.Thread(target=self.vehicle.start_driving,args=(start,destination),)
        trip_thread.start()
        self.vehicle.start_driving(start,destination)
        self.location=destination
      
rider1=Rider('rider1','rider1@gmail.com','RiderOne',randint(0,30),1000)
rider2=Rider('rider2','rider2@gmail.com','RideTwo',randint(0,30),1000)
rider3=Rider('rider3','rider3@gmail.com','RiderThree',randint(0,30),1000)
rider4=Rider('rider4','rider4@gmail.com','RiderFour',randint(0,30),1000)
rider5=Rider('rider5','rider5@gmail.com','RiderFive',randint(0,30),1000)

vehicles_type=['car','bike','cng']
for i in range(1,100):
    driver1=Driver(f'driver{i}',f'driver{i}@gmail.com',f'Driver{i}',randint(0,30),randint(1000,5000))
    driver1.take_driving_test()
    driver1.register_vehicle(choice(vehicles_type),randint(1000,5000),110)

print(uber.get_available_Cars)
uber.find_a_vehicle(rider1,choice(vehicles_type),50)
uber.find_a_vehicle(rider2,choice(vehicles_type),50)
uber.find_a_vehicle(rider3,choice(vehicles_type),50)
uber.find_a_vehicle(rider1,choice(vehicles_type),50)
uber.find_a_vehicle(rider2,choice(vehicles_type),50)

print(rider1.get_trip_history())
print(uber.total_income())
