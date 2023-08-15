
import time
from functools import cache

@cache
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

start=time.time()

for i in range(35):
    print(i  , fib(i))
end=time.time()
net_time=(end-start)*1000

print('Net time :',net_time)