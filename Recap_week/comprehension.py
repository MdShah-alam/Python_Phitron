# list , dictionary comprehensions

# list comprehensions
# # [expression for item in range()]

# # Example -1
# lst=["hello","world","python"]
# new_lst=[x.upper() for x in lst]
# print(new_lst)

# # Example -2
# x=[i for i in range(1,10)]
# y=list(range(1,10))
# print(x)
# print(y)

# # Example -3
# lst=[x for x in range(1,6) if x%2==0]
# print(lst)

# # Example -4
# lst=[x for x in range(100) if x%3==0 if x%5==0]
# print(lst)

# # Example -5
# lst=["Even" if x%2==0 else "Odd" for x in range(20)]
# print(lst)

# # Example -6
# lst=[(x,y) for x in [1,3,5,7] for y in [2,3,4,5] if x!=y]
# print(lst)

# Dictionary comprehensions

# # Example -1
# dct={i:i+1 for i in range(5)}
# print(dct)

# # Example -2
# dct = {"jack":30, "rahim":22,"karim":21}
# new_dct={k:v for k,v in dct.items() if v%2==0}
# print(new_dct)

# # Example -3
# dct = {"jack":30, "rahim":22,"karim":21}
# new_dct={k:v for k,v in dct.items() if v%2==0 if v>25}
# print(new_dct)

# # Example -4
# dct={"jack":60,"rahim":23,"karim":25}
# new_dct={k:('old'if v>40 else 'young') for k,v in dct.items()}
# print(new_dct)

# # Example -5
# dct={k1 : {k2 : k1*k2} for k2 in range(6) for k1 in range(5)}
# print(dct)


# # question-2
# dct={k1 : [x for x in range(1,6) if k1!=x] for k1 in range(1,6)}
# print(dct)

# question-3
# # Scope are four type:
# # There are =
# # 1. Local
# # 2. Enclosed
# # 3. global
# # 4. Builtin

# from math import pi      # builtin scope value
# pi=23.50     # Global scope 
# def first_scope():
#     pi=20.50    # Enclosed scope
#     def second_scope():
#         pi=15.50    # Local scope
#     second_scope()
# first_scope()

# question-5

# data=[{'a':5,'b':10},{'x':15,'y':20}]
# for val in data:
#     for key,val2 in val.items():
#         print(f'Key:{key} Value:{val[key]}')

data={
    'a':[{
        'aa':{'aax':5,'aay':6,'aaz':7},
        'ab':{'abx':8,'aby':9,'abz':10}
        },
        {
        'aaa':{'aaax':11,'aaay':12,'aaaz':13},
        'aab':{'aabx':14,'aaby':15,'aabz':16}
        }],
    'b':[{
        'ba':{'bax':17,'bay':18,'baz':19},
        'bb':{'bbx':20,'bby':21,'bbz':22}
        },
        {
        'bba':{'bbax':23,'bbay':24,'bbaz':25},
        'bbb':{'bbbx':26,'bbby':27,'bbbz':28}
        }],
    'c':[{
        'ca':{'cax':29,'cay':30,'caz':31},
        'cb':{'cbx':32,'cby':33,'cbz':34}
        },
        {
        'cca':{'ccax':35,'ccay':36,'ccaz':37},
        'ccb':{'ccbx':38,'ccby':39,'ccbz':40}
        }]
}

for key1,val1 in data.items():
    for val2 in val1:
        for key2,val3 in val2.items():
            for key3,val4 in val3.items():
                print(f'Key:{key3} Value:{val3[key3]}')

# question-7

# lst=[ x for x in range(20) if x%3==0 if x!=0 ]
# print(lst)

