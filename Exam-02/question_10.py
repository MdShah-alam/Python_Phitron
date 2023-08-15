

from cmath import sqrt


class Distance:
    def __init__(self,x1,x2,y1,y2) -> None:
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        
    def dist(self):
        return sqrt(pow((self.x2-self.x1),2)+pow((self.y2-self.y1),2))

x1=int(input('Enter a number : '))
x2=int(input('Enter a number : '))
y1=int(input('Enter a number : '))
y2=int(input('Enter a number : '))

dis=Distance(x1,x2,y1,y2)
print(dis.dist())
