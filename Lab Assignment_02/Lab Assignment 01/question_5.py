
def create_list(x):
    lst=[]
    for key,value in x.items():
        lst.append(key)
        lst.append(value)
        
    return lst

d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
new_list=create_list(d)
print(new_list)
