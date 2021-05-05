t = int(input())

while t:
    
    
    n = int(input())
    axx = list(map(int,input().split()))
    
    d = {}
    
    c = 0
    
    for i in range(n):
        diff = axx[i] - i
        if diff in d:
            c+=d[diff]
        
        if diff not in d:
            d[diff] = 0
        
        d[diff] += 1   
        
    print(c)  
    
    t-=1