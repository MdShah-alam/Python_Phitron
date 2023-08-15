
# sum_list = [] initialize result list.
# for (item1, item2) in zip(list1, list2):
# sum_list. append(item1+item2)
# print(sum_list) [(1 + 4), (2 + 5), (3 + 6)]

# list1 = ["M", "na", "i", "Bo"]
# list2 = ["y", "me", "s", "nd"]
# list3=[]
# for (list1,list2) in zip(list1,list2):
#     list3.append(list1+list2)
    
# print(list3)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()

# list3=[]
# for (list1,list2) in zip(list1,list2):
#     print(list1 ,list2)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
c = dict(zip(keys, values))
print(c)