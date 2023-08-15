
import time
class School:
    #constractor
    def __init__(self,name,address,principal='') -> None:
        self.name=name
        self.address=address
        self.principal=principal
        self.grade=[]
        
    def add_grade(self,name,teacher):
       new_grade=Grade(name,teacher)
       self.grade.append(new_grade)
       
    def remove(self, name):
        idx=0
        for i,grad in enumerate(self.grade):
            if name==grad.name:
                idx=i
                
        del self.grade[idx]
       
       
class Grade:
    # constractor
    def __init__(self,name,teacher) -> None:
        self.strudents=[]
        self.name=name
        self.teacher=teacher
        
    def __repr__(self) -> str:
        return f'class {self.name} with teacher {self.teacher}'
    
    def __del__(self):
        print(f'deleting {self.name}  with teacher {self.teacher}')
             
        
oxfrod=School('Abul basar','Thakurgaon','Rahim')
oxfrod.add_grade('class 3','Roni')
oxfrod.add_grade('class 5','Royal')
oxfrod.add_grade('class 6','Raju')
print(oxfrod.grade)
oxfrod.remove('class 5')
time.sleep(10)

print(oxfrod.grade)