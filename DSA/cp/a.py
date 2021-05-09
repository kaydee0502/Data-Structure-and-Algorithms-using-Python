t = int(input())

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

while t:
    
    n = int(input())
    a = list(map(int,input().split()))
    
    res = []
    
    
    for i in range(1,n):
        if i == 1:
            m = min(a[i],a[i-1])
            a[i-1] = m
            a[i] = m+1
            
        else:
            m = a[i-1]
            a[i] = m+1
            
        
       
    
        res.append([i,i+1,m,m+1])

         
         
    #print(*a)
    print(len(res))
    if res:
        for i in res:
            print(*i)
            
    
    
    
    t-=1