n=int(input('Enter the numbers of days : '))
rainfall=[]
for i in range(n):
    rain=int(input(f'Enter {i+1} day rainfall data : '))
    rainfall.append(rain)

maximum=rainfall[0]
minimum=rainfall[0]
for i in range(n):
    if maximum<rainfall[i]:
        maximum=rainfall[i]
    if minimum>rainfall[i]:
        minimum=rainfall[i]
        
print(f'Maximum rainfall is : {maximum}')
print(f'Minimum rainfall is : {minimum}')