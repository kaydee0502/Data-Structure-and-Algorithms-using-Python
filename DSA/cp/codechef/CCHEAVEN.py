MOD = 10**9 + 7



def seq(arr, index, s,ans): 
        
    if index == len(arr): 
        if len(subarr) != 0: 
            ans.append(s)
    else: 
        seq(arr, index + 1, s,ans) 
        seq(arr, index + 1, s+[arr[index]],ans) 
    
def inter(a,b,arr):
    count = 0
    for i in a:
        for j in b:
            count += arr[i-1][j-1]
    return count

t = int(input())

while t:
    n,m,B = map(int,input().split())
    mat = []
    for i in range(n):
        r = list(map(int,input().split()))
        mat.append(r)
    
    
    r = []
    seq([i for i in range(1,n+1)],0,[],r)
    
    c = []
    seq([i for i in range(1,m+1)],0,[],c)
    
    
    count = 0
    
    for i in r:
        for j in c:
            
            if inter(i,j,mat) == B:
                
                count += 1
    
    print(count%MOD)
    t-=1