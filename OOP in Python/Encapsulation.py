
class Account:
    def __init__(self,holder,initial_balance) -> None:
        self.holder=holder #public
        self._id=165
        self.__balance=initial_balance
        
    def deposite(self,amount):
        print(f'adding {amount} to your account')
        self.__balance+=amount
        
    def withdraw(self,amount):
        print(f'widthdraw {amount} from your account')
        self.__balance-=amount
        
        
class StudentAccount(Account):
    def __init__(self,holder,initail_balance,school):
        self.school=school
        super().__init__(holder,initail_balance)
        
    def get_balance(self):
        return f'Your balance is {self.__balance}'
        
rafsan=StudentAccount('rafsan',50000,'IUB')
# print(rafsan.__balance)
rafsan.deposite(20000)
rafsan.deposite(15000)
# rafsan.__balance=0
# print(rafsan.get_balance())
print(rafsan._id)

print(rafsan.holder)
        