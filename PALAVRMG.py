#by douglascost47

n = int(input())

while(n):
    s = input()      
    notord = s.lower()
    notord = [c for c in notord]        

    ans = True
    for i in range(0, len(notord) - 1):
        if(notord[i] >= notord[i+1]):
            ans = False

    print(s + ':', end=' ')
    print('O' if ans else 'N')

    n-=1