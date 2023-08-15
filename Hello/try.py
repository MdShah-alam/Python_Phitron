# try:
#     num=15/4
#     print(num)
# except:
#     print('This can not divisior')
# finally:
#     print('this is done')

# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occurred")
# except "someError":
#     print ("someError has occurred")
# def f1():
#     global x
#     x+=1
#     print(x)
# x=12
# print("x")
def display(**kwargs):
    for i in kwargs:
        print(i, end=” ”)