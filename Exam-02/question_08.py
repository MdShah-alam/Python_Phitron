
a=[]
n=int(input('Enter a number :'))
for i in range(0,n):
    b=int(input('Enter value :'))
    a.append(b)
    
print(a)  
 
target=int(input('Target : '))

num=len(a)
for i in range(0,num):
    for k in range(i+1,num):
        sum = a[i]+a[k]
        if sum==target:
            print(i+1 , k+1)
            
#  [10,20,10,40,50,60,70]
    