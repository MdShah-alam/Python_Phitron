
class St:
    def __init__(self,x,n) -> None:
        self.x=x
        self.n=n
        
    def sum(self):
        return self.x+self.n
    
    def pow(self):
        return pow(self.x,self.n)
    
    
x=int(input('Enter a number : '))
n=int(input('Enter a number : '))

st=St(x,n)
print(st.sum())
print(st.pow())