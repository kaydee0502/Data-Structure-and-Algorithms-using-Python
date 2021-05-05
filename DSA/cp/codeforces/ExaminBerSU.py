import heapq

n,k = map(int,input().split())
arr = list(map(int,input().split()))


res = []

pref = 0

for i in range(len(arr)):
    pref += arr[i]
    
    if pref > k:
        c = 0
        p = pref
        a = list(map(lambda x : -x,arr[:i]))
        heapq.heapify(a)
        #print(p,a)
        while p > k:
            p += heapq.heappop(a)
            c+=1
            
        res.append(c)
        
    else:
        res.append(0)
        
print(*res)
        
        
        
        
