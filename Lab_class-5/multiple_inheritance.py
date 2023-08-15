
class School:
    def __init__(self,school_name) -> None:
        self.school_name=school_name
    def __repr__(self) -> str:
        return f'School name is {self.school_name}'
    
class Teacher:
    def __init__(self,teacher_name) -> None:
        self.teacher_name=teacher_name
    def __repr__(self) -> str:
        return f'Teacher name is {self.teacher_name}'
    
class Student(Teacher,School):
    def __init__(self, name,teacher_name,school_name) -> None:
        Teacher.__init__(self,teacher_name)
        School.__init__(self,school_name)
        self.name=name
        
    def __repr__(self) -> str:
        return f'Student name is {self.name}'
        
student=Student('sakib','Mis Runa','Trust school')
print(student)
print(student.teacher_name)
print(student.school_name)