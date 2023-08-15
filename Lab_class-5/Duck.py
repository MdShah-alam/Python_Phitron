
class Teacher:
    def __init__(self,teacher_name) -> None:
        self.teacher_name=teacher_name
        self.students=[]
        
    def entry_student(self,studentObj):
        self.students.append(studentObj)
        
class Student:
    def __init__(self,student_name) -> None:
        self.student_name=student_name
        
    def enter_in_teacher(self,teacherObj):
        teacherObj.students.append(self)
        
    def __repr__(self) -> str:
        return f'Student ({self.student_name})'

soleman_sir=Teacher('Soleman mia')
mis_rahima=Teacher('Mis Rahima')
rahim_mia=Teacher('Rahim Mia')
student=Student('rahim')
student.enter_in_teacher(rahim_mia)
student.enter_in_teacher(mis_rahima)
print(rahim_mia.students)
print(mis_rahima.students)
    