
class Trip:
    def __init__(self,trip_cites,start_trip) -> None:
        self.trip_cites=trip_cites
        self.start_trip=start_trip
        self.aircrafts=None
        self.route=None
        self.cost=None
        
    def __repr__(self) -> str:
        return f'Trip {self.trip_cites} Aircrafts {self.aircrafts} route {self.route} cost {self.cost} .'
    