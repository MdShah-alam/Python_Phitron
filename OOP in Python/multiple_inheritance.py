
class School:
    def __init__(self,name) -> None:
        self.school_name=name
        print('School init is called')
        
class Grade:
    def __init__(self,grade_name):
        self.grade_name=grade_name
        print('Grade init is called')
        
class SportTeam:
    def __init__(self,sport_name) -> None:
        self.sport_name=sport_name
        self.team=[]
        
    def add_player(self,player_name):
        self.team.append(player_name)
        
        
class Student(School,Grade,SportTeam):
    def __init__(self,name,grade_name,school_name,sport_name):
        self.name=name
        Grade.__init__(self,grade_name)
        School.__init__(self,school_name)
        SportTeam.__init__(self,sport_name)
        print('Student init is called')

ananta_j=Student('AJ','MBA','UK','Criket')
print(ananta_j.name)
print(ananta_j.grade_name)
print(ananta_j.school_name)
ananta_j.add_player('Borsha')
ananta_j.add_player('AJ')
print(ananta_j.team)

