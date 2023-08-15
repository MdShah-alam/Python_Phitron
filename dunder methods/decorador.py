
import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('Time start')
        start=time.time()
        start=start*10000
        func(*args,**kwargs)
        end=time.time()
        end=end*10000
        print(f'Time end , total time is : {end-start} .')
    return inner
  
@timer      
def get_factorial(n):
    result=math.factorial(n)
    print(f'factorial of {n} is : {result} ')
get_factorial(n=100)
    
# timer(get_factorial)()