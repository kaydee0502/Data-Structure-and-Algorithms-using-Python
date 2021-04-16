N = int(input())

arr = list(map(int,input().split()))

q=int(input())
zero = {}


for i in range(q):
    x,k = map(int,input().split())
    dist = 0
    x= x-1
    
    
    start = x
    
    
    while k > 0 and x < N:
        
        if x in zero:
            if zero[x] == -1:
                break
            
            else:
                stop = zero[x]
                dist += arr[stop]*()
                
                
                pass
        
        
        if k >= arr[x]:
            dist += arr[x]*(x-start)
            k-=arr[x]
            arr[x] = 0
            
            
            
        else:
            zero[start] = x
            dist += k*(x-start)
            arr[x] -= k
            
            
        #print(k)
        
        x+=1
    
    if not zero[start]:
        zero[start] = -1
        
        
    print(dist)
        
        
    
    
