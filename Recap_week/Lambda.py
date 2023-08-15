# variable=lambda argument:expression

# # Example -1
# s="Phitron"
# new_string = lambda string : string.upper()[::-1]
# print(new_string(s))

# # Example -2
# max=lambda a,b:a if(a>b) else b
# print(max(max(10,20),max(30,(max(3,4)))))

# # Example -3
# lst=[1,2,3,4,5,6,7]
# new_lst=[lambda arg=x:arg*2 for x in lst]
# for i in new_lst:
#     print(i(),end=" ")

# # Example -4
# # filter , map , reduce 

# my_lst=[1,2,3,4,5,6]
# new_lst=list(filter(lambda x: (x%2 == 0), my_lst))
# print(new_lst)

# # Example -5
# string_list=["hello","world","python","shah_alam"]
# new_list=list(map(lambda x: x.upper(),string_list))
# print(new_list)

# # Example -6
# from functools import reduce
# lst=[1,2,3,4,5,6,7,8,9,10]
# sum=reduce(lambda x,y:x+y,lst)
# print(sum)

# question-8
# even_odd=lambda x:'Yes' if( x % 2 ==0) else 'No'
# print(even_odd(6))

# question-9

# def f1():
#     try:
#         for i in range(5):
#             print(f"f1 - {i}")
#     except:
#         print('Error found')
#     else:
#         print('No Error found')
#     finally:
#         print('I always print')
 
# def f2():
#     try:
#         for i in range(5):
#             print(f"f2 - {i}")
#     except:
#         print('Error found')
#     else:
#         print('No Error found')
#     finally:
#         print('I always print')
 
# def f3():
#     try:
#         for i in range(5):
#             print(f"f3 - {i}")
#     except:
#         print('Error found')
#     else:
#         print('No Error found')
#     finally:
#         print('I always print')
       
# def f4():
#     try:
#         for i in range(5):
#             print(f"f4 - {i}")
#     except:
#         print('Error found')
#     else:
#         print('No Error found')
#     finally:
#         print('I always print')
        
# f1()
# f2()
# f3()
# f4()


# question-10

class Grandparent:
    def __init__(self) -> None:
        pass

class Parent():
    def __init__(self) -> None:
        pass
    
class Child(Parent,Grandparent):
    def __init__(self) -> None:
        self.hi='Hi'
        Parent.__init__(self)
        Grandparent.__init__(self)