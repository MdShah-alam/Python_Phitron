
# print(max(32,45,54,67,32,12,87))
# print(max([32,54,76]))
# print(max('roni','shah','sakib'))

# def add(num1,num2,num3=0,num4=0):
#     return num1+num2+num3+num4

# print(add(34,12))
# print(add(34,12,3))
# print(add(34,12,3,54))


def add2(*args):
    sum =0
    for i in args:
        sum+=i
    return sum


print(add2(43,5,32,12,34))

# operator overloading

print(32+34)
print('H'+'W')

class Account:
    def __init__(self,holder,balance) -> None:
        self.holder=holder
        self.balance=balance
        
    def __add__(self,other):
        return self.balance + other.balance
    
    def __eq__(self,other:object):
        return self.balance==other.balance
        
my_account=Account('Sakib Al Hasan',50000)
her_account=Account('Shishir vabi',70000)
result=my_account+her_account
print(result)
        