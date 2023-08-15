
import csv
from airport import Airprt
from math import sin , cos,atan2,sqrt

class Allairprot:
    def __init__(self) -> None:
        self.land_airport_data('./airport.csv')
        self.airports={}
    
    def land_airport_data(self,file_path):
        airports={}
        currency_rate={}
        country_currency={}
        
        #get currency name <---> rate
        with open('./currencyrate.csv','r') as file:
            lines=csv.reader(file)
            for line in lines:
                currency_rate[line[1]]=line[2]
        file.close()
        
        # dictionary country <------->currency name
        with open('./countrycurrency.csv','r') as file:
            lines=csv.reader(file)
            # print(lines)
            for line in lines:
                country_currency[line[0]]=line[1]
        file.close()
        
        with open(file_path,'r',encoding='utf8') as file:
            lines=csv.reader(file)
            try: 
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rate[currency]
                    airports[line[4]] = Airprt(line[4], line[1], line[2], line[3], line[6], line[7], rate)
            except KeyError as e:
                print('key not found', e)
        # print(self.airports)
            # for airports in airports.items():
            #     print(airports)
                
    def get_distance_between_two_airport(self,lat1,lon1,lat2,lon2):
        radius=6371
        lat_diff = radius(lat1 - lat2)
        lon_diff= radius(lon1 - lon2)
        arc=(sin(lat_diff/2)*sin(lat_diff/2))+(cos(radius(lat1))*cos(radius(lat2))*sin(lon_diff/2)*sin(lon_diff/2))
        c=2*atan2(sqrt(arc),sqrt(1-arc))
        distance=radius*c
        return distance
    
    def distance_between_two_airports(self,airport1_code,airport2_code):
        print(self.airports)
        airport1=self.airports[airport1_code]
        airport2=self.airports[airport2_code]
        distance=self.get_distance_between_two_airport(airport1.lat,airport1.lon,airport2.lat,airport2.lon)
        return distance
    
    def get_ticket_price(self,start,end):
        # print(start , end)
        distance=self.distance_between_two_airports(start,end)
        airport1=self.airports[start]
        fare=distance*airport1.rate
        return fare
        
# Allairprot()              
world_tour=Allairprot()
fare=world_tour.get_ticket_price('IDA','PRA')
print('ticket fare is : ',fare)