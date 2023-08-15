

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
        
    def borrow_book(self,bookname,user):
        for book in self.book_list:
            if book==bookname:
                if bookname in user.borrow_books:
                    print('Age ferot daw')
                    return
                if self.book_list[book]==0:
                    print('sorry insufficient book')
                    return
                self.book_list[book]-=1
                user.borrow_books.append(bookname)
                print('Borrow book successfully')
                return
        print('book not available')
        
    def returned_book(self,bookname,user):
        for book in self.book_list:
            if book==bookname:
                if book in user.borrow_books:
                    self.book_list[book]+=1
                    user.borrow_books.remove(bookname)
                    user.returned_books.append(bookname)
                    return
                else:
                    print('Thanks but others books not allow')
        print('This book is not for this libary')
        
    def donate(self,bookname,amount):
        for book in self.book_list:
            if book==bookname:
                self.book_list[book]+=amount
                print('Thanks for donate')
                return
        self.book_list[bookname]=amount
        print('Thanks for donate')

            
    def available(self):
        for book in self.book_list:
            if self.book_list[book]>0:
                print(book , self.book_list[book]) 
        
libary=Libary({'English': 2,'Bangla' : 5,'Math' :2})          
alluser=[]
currentuser=None

while True:
    if currentuser==None:
        print('Not logged in \nPlease login or create an account (L/C) : ')
        option=input('Enter : ')
        if option=='L':
            roll=int(input('Enter roll : '))
            password=input('Enter password : ')
            match=False
            for user in alluser:
                if user.roll==roll and user.password==password:
                    currentuser=user
                    match=True
                                    
            if match==False:
                print('No user found')
        else:
            name=input('Enter name : ')
            roll=int(input('Enter roll : '))
            password=input('Enter password : ')
            found=False
            for user in alluser:
                if user.roll==roll:
                    found=True
            if found:
                print('You created an account before')
                continue
            user=User(name,roll,password)
            currerntuser=user
            alluser.append(user)
    else:
        print('\n   OPTIONS   ')
        print('--------------')
        print('1. borrow a book')
        print('2. return a book')
        print('3. Borrowed books list')
        print('4. returned books list')
        print('5. Check available')
        print('6. donate ')
        print('7. Logout ')
        x=int(input('Enter your choice :'))
        if x==1:
            bookname=input('Enter book name :')
            libary.borrow_book(bookname,currentuser)
        
        elif x==2:
            bookname=input('Enter book name :')
            libary.returned_book(bookname,currentuser)
            
        elif x==3:
            print(currentuser.borrow_books)
            
        elif x==4:
            print(currentuser.returned_books)
            
        elif x==5:
            libary.available()
        
        elif x==6:
            bookname=input('Enter book name :')
            amount=int(input('Enter the amount of book :'))
            libary.donate(bookname,amount)
            
        elif x==7:
            currentuser=None
