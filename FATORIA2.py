#by douglascost47

def fat(n):
    ans = 1
    for i in range(1, n+1):        
        ans = ans * i
    return ans
    

print(fat(int(input())))