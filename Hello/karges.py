# def add(num1,num2,*numbers):
#     print(num1 , num2)
#     print(numbers)

# add(2,4,5,6,7,1)

# def full_name(f_name,l_name):
#     result=f'{f_name}  {l_name}'
#     return result

# name=full_name(l_name='Chowdhury' , f_name='Choto')
# # print('\n',name,'\n')

# def long_name(**karges):
#     # print('\n',karges,'\n')

# long_name(first='Dr .',last='Chowdhury',middle='Rahman')


# def mix_name(f_name,**name_parts):
#     print(f_name)
#     print(name_parts)

# mix_name(arge='chowdhury',f_name='Dr . ',middle='choto',last='Farhan')

def multiply(*numbers):
    result=1
    for num in numbers:
        result=result*num
    return result

# result=multiply(5,6,7,3,2)
# print(result)


# def all_type(name , *arge, **karge):
#     print(name)
#     for word in arge:
#         print(word)
#     for key,value in karge.items():
#         print(key  , value)

# all_type('kamal','sssss','kkkk','fff',f_name='Dr.',m_name='Choto',l_name='Chowdhury')