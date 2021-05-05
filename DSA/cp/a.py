t = int(input())

while t:
    
    
    n = int(input())
    if n == 2:
        print(-1)
        t-=1
        continue
        
    mat = [[0 for i in range(n)] for j in range(n)]
    
    c = 1
    for i in range(n):
        for j in range(n):
            
            if (i+j)%2 == 0:
              
                mat[i][j] = c
                c+=1
                
    
    for i in range(n):
        for j in range(n):
            
            if mat[i][j] == 0:
                
                mat[i][j] = c
                c+=1
            
    for i in mat:
        print(*i)
    
    t-=1