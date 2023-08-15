
class User:
    def __init__(self,name,roll,password):
          self.name=name
          self.roll=roll
          self.password=password
          self.borrow_books= []
          self.returned_books=[]
 
class Libary:
    def __init__(self,book_list):
        self.book_list=book_list
        
libary=Libary({'English': 2,'Bangla' : 5,'Math' :3})          
alluser=[]
currentuser=None

while True:
    if currentuser==None:
        print('No Logged \nPlease login or create (L/C) : ')
        option=input("Enter : ")
        if option=='L':
            roll=int(input("Roll :"))
            password=input('password :')
            match=True
            for user in alluser:
                if user.password==password and user.roll==roll:
                    currentuser=user
                    match=False
            if match==True:
                print("Not found")
        else:
            name=input("Name :")
            roll=int(input("Roll :"))
            password=input('Password :')
            use=User(name,roll,password)
            print('Hello')
            currentuser=use
    else:
        print('All ok')
        break
            
        