# problem-1
# string =  'pHitrOn.iO presents "Python COuRSe".'
# size = len(string)
# print('\n',size)

# new_string=''

# for i in range(0,36,1):
#     if (string[i]>='a' and string[i]<='z'):
#         new_string+=chr(ord(string[i])-32)
#     elif (string[i]>='A' and string[i]<='Z'):
#         new_string+=chr(ord(string[i])+32)
#     else:
#         new_string+=string[i]

# #  PhITRoN.Io PRENSENTS “pYTHON coUrsE”

# print(new_string,'\n')

# problem - 2
# number=int(input())
# for i in range(1,number+1,1):
#     for k in range(1,i+1,1):
#         print(k,end='  ')
#     print('\n')

# problem -3
# number=int(input())
# first_number=0
# second_number=1
# fibonacci=0

# for count in range(0,number,1):
#     if count<=1:
#         fibonacci=count
#     else:
#         fibonacci=first_number+second_number
#         first_number=second_number
#         second_number=fibonacci
#     print(fibonacci,end=" ")

# pratice - 4
# string="P@#yn26at^&i5ve"
# size=len(string)
# print(size)
# lowercase=0
# uppercase=0
# digit=0
# symble=0

# for i in range(0,size,1):
#     if string[i]>='a' and string[i]<='z':
#         lowercase+=1
#     elif string[i]>='A' and string[i]<='Z':
#         uppercase+=1
#     elif string[i]>='0' and string[i]<='9':
#         digit+=1
#     else:
#         symble+=1

# print('Uppercase = ',uppercase)
# print('Lowercase = ',lowercase)
# print('Digit = ',digit)
# print('symble = ',symble)

# # problem - 5
# string1="Abc"
# string2="Xyz"
# string3=""

# size1=len(string1)
# size2=len(string2)
# j=size2-1
# for i in range(0,size1,1):
#      string3+=string1[i]+string2[j]
#      j-=1

# print(string3)

# practice-6

# string1="Phi"
# string2="Phitron"
# size1=len(string1)
# size2=len(string2)
# count=0

# for i in range(0,size2,1):
#     for k in range(0,size1,1):
#         if string1[k]==string2[i]:
#             count+=1

# if count==size1:
#     print("\nTrue\n")
# else:
#     print("\nFalse\n")

# practice-7
# number=int(input())
# save_number=number
# p_number=0

# while number!=0:
#     digit=int(number%10)
#     p_number=p_number*10+digit
#     number=int(number/10)
# if p_number==save_number:
#     print("\nTrue \n")
# else:
#     print("\nFalse \n")

# practice - 8

# first_num=int(input())
# last_num=int(input())

# for n in range(first_num, last_num+1,1):
#     count=0
#     for i in range(2,n,1):
#         if n%i==0:
#             count=1
#             continue
#     if count==0:
#         print(n)

# # practice - 9
# number=int(input())

# for i in range(1,number+1,1):
#     for k in range(1,i,1):
#         print('*',end=" ")
#     print('\n')
# for i in range(number-1,0,-1):
#     for k in range(i,0,-1):
#         print('*',end=" ")
#     print('\n')
