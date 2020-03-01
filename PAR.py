#by douglascost47
N = int(input())
t = 1
while(N):
    a = input()
    b = input()

    print('Teste ' + str(t))
    while(N):
        x,y = [int(x) for x in input().split()]        
        print(a if((x+y)%2 == 0) else b)        
        N-=1
    
    print()
    t+=1
    N = int(input())