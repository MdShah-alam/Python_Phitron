
import random

class BRTA:
    def __init__(self):
        self.__license={}
        
    def take_driving_test(self,email):
        score=random.randint(0,100)
        if score >= 33:
            # print('congrats , you have passed', score)
            license_number=random.randint(5000,10000)
            self.__license[email]=license_number
            return license_number         
        else:
            # print('sorry you failed ',score)
            return False
        
    def valideta_license(self,email,license):
        for key , value in self.__license.items():
            if key==email and value == license:
                return True
            return False
        
        