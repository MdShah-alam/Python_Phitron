
from TravelAgent import TravelAgent

def main():
    travel_agent=TravelAgent('Go Go sun')
    trip_info1=travel_agent.set_trip_one_city_one_way('DAC','PRA','05/06/2023')
    print('aircraft ',trip_info1[0])
    print('price ',trip_info1[1])

if __name__=='__main__':
    main()