
from All_airport import Allairprot
from All_airlines import Airlines
class TravelAgent:
    def __init__(self,name) -> None:
        self.name=name
        self.trips=None
        self.air_crafts=Allairprot()
        self.air_lines=Airlines()
    '''
    pramas
    strat=starting airport
    end=ending airport
    travel data=traveling data
    return 
    cost , aircraft
    
    '''
    def set_trip_one_city_one_way(self,start,end,start_data):
        price=self.air_crafts.get_ticket_price(start,end)
        distance=self.air_crafts.distance_between_two_airports(start,end)
        aircraft=self.air_lines.get_aircraft_by_distance(distance)
        return [aircraft,price]
        pass
    
    def set_trip_one_city_two_way(self):
        pass
    
    def set_trip_multicites_one_way(self):
        pass
    
    def set_trip_multicites_two_ways(self):
        pass
    
    def __repr__(self) -> str:
        return f'Travel Agent {self.name} Trip {self.trips}'
        
    