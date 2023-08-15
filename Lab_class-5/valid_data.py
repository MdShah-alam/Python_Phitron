# Attributes validation using ' assert '
class Persion:
    def __init__(self,name,phone,age) -> None:
        assert age>13 , f'Only gearter than 13 is accepted'
        assert len(phone)==11, f'phone lenght can not less than or greater than 11'
        self.name=name
        self.phone=phone
        self.age=age
        
    def __repr__(self) -> str:
        return f'Name : {self.name} , Phone : {self.phone} , Age : {self.age}'
    
user=Persion('Shah_alam','01234567890',20)
print(user)
