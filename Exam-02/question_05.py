
inpu=open('sin.txt','a')
n=int(input('Enter : '))
name=[]
mark=[]
id=[]
for i in range(0,n):
    student_name=input("Enter name : ")
    mark_=input('Enter mark : ')
    student_id=input('Enter id : ')
    name.append(student_name)
    mark.append(mark_)
    id.append(student_id)

lenght=len(name)
for i in range(0,lenght):
    st=name[i]+' '+mark[i]+' '+id[i]+'\n'
    inpu.write(st)
    
# for line in output.readlines():
#     for word in line.split(' '):
#         print(word)
    
    
