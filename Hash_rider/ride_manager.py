

class RideManager:
    def __init__(self) -> None:
        print('Ride manager is actived')
        self.__income=0
        self.__trip_history=[]
        self.__availablevehicles_car=[]
        self.__availablevehicles_bike=[]
        self.__availablevehicles_cng=[]

    def add_a_vehicle(self,vehicle_type,vehicle):
        if vehicle_type=='car':
            self.__availablevehicles_car.append(vehicle)
            
        elif vehicle_type=='bike':
            self.__availablevehicles_bike.append(vehicle)
            
        else:
            self.__availablevehicles_cng.append(vehicle)
    
    def get_available_Cars(self):
        return self.__availablevehicles_car
    
    def total_income(self):
        return self.__income
    
    def get_history(self):
        return self.__trip_history
    
    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type=='car':
            vehicles=self.__availablevehicles_car
        elif vehicle_type=='bike':
            vehicles=self.__availablevehicles_bike
        else:
            vehicles=self.__availablevehicles_cng
        if len(vehicles)==0:
            print(f'sorry no {vehicle_type} available')
            return False
        for vehicle in vehicles:
            # print('potential',rider.location,vehicle.driver.location)
            if abs(rider.location-vehicle.driver.location)<10:
                distance=abs(rider.location-vehicle.driver.location)
                fare=distance * vehicle.rate
                if rider.balance < fare:
                    print(f'insaficient balance , fare : {fare} , balance : {rider.balance}')
                    return False
                if vehicle.status=='available':
                    trip_info=f'Match {vehicle_type} you {rider.name} for fare {fare} with {vehicle.driver.name} started :{rider.location} to :{vehicle.driver.location}'
                    print(trip_info)
                    vehicles.remove(vehicle)
                    rider.start_trip(fare,trip_info)
                    vehicle.driver.start_trip(rider.location,destination,fare * 0.8,trip_info)
                    self.__income += fare * 0.2
                    self.__trip_history.append(trip_info)
                    return True 
        print('looking done')
    
uber=RideManager()
  