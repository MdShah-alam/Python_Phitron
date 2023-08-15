num=input('Enter input : ')
print(num)
print(type(num))
num=int(num)
print(type(num))

while num==0 or num<0 or num>0:
    if num>0:
        about_num=f'{num} is positive '
        print(about_num)
    elif num<0:
        about_num=f'{num} is negative '
        print(about_num)
    num=input()
    if num=='Quit':
        break
    else:
        num=int(num)

