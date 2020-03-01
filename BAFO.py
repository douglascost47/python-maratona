#by douglascost47

R = int(input())

test = 1

while(R):

    ans = 0
    while(R):
        a,b = [int(x) for x in input().split()]
        ans = ans - a + b
        R-=1
    
    print('Teste ' + str(test))
    print('Aldo' if(ans < 0) else 'Beto')
    print()
    test+= 1
    R = int(input())