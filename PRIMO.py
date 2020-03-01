#by douglascost47
import math  

def check(n): 
    if n == 1: 
        return False
          
    # from 1 to sqrt(n)
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True

n = int(input())
print('sim' if(check(n)) else 'nao')