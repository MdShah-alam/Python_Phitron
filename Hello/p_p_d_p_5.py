#  for num in range(5,45,5)
for i in range(1,50,1):
    if(i%3==0 and i%5==0):
        print('Fizzbuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)