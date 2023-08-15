import csv
result=0
with open('./data/currencyrate.csv','r') as file:
    lines=csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(type(line[3]))
    
    print(result)