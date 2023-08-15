
class Account:
    def __init__(self,holder) -> None:
        self._account_holder=holder
        
class StudentAccount(Account):
    def __init__(self,name,balance,holder) -> None:
        self.name=name
        self.__balance=balance
        super().__init__(holder)
        
    def deposite(self,amount):
        self.__balance+=amount
        
    def withdraw(self,amount):
        self.__balance-=amount
        
    def get_balance(self):
        return self.__balance
    
nas=StudentAccount('Nas daily',12000,'Nas Academy')
print(nas.get_balance())
nas.deposite(50000)
nas.deposite(38000)
print(nas.get_balance())
# print(dir(nas))
# print(nas.__balance)
print(nas._StudentAccount__balance)
