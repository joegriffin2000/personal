#random centered randint
import random as rand
import math

def randint_centered(N,dev='sqrt'):
    high=None
    low=None
    
    if isinstance(dev,str):
        match dev:
            case 'sqrt':
                high = float(N) + math.sqrt(N)
                low = float(N) - math.sqrt(N)
            case 'log':
                high = float(N) + math.log(N)
                low = float(N) - math.log(N)
            case _:
                raise ValueError(f"unrecognized string for argument'dev': '{dev}'")        
        high,low = int(high),int(low)
    elif isinstance(dev,int):
        high = N + dev
        low = N - dev
    else:
        raise TypeError(f"argument 'dev' can only be of type int or str: '{dev}'")
    
    return rand.randrange(low,high+1)
    
num = 81
ls = list()
for i in range(0,10):
    ls.append(randint_centered(num))
ls.sort()
print(num,ls)