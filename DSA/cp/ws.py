
import string


w = {x:y for x,y in zip(string.ascii_lowercase,[i for i in range(1,27)])}


def solve(s):
    u = {}
    l = {}
    
    for i in s:
        if i.islower():
            if not i in l:
                l[i] = 0
            l[i] +=1
        else:
            if not i in u:
                u[i] = 0
                
            u[i] += 1
            
    
    for i in l:
        l[i] = [l[i]*w[i.lower()],l[i]]
        
    for i in u:
        u[i] = [u[i]*w[i.lower()],u[i]]
        
    
    
    ls = []
    us = []
    for i in l:
        ls.append((l[i][0],l[i][1],i))
        
    for i in u:
        us.append((u[i][0],u[i][1],i))
        
    ls.sort(key = lambda x : (x[0], -x[1], x[2]))
    us.sort(key = lambda x : (x[0], -x[1], x[2]))
    i = 0
    j = 0
    res = ""
    
    while i < len(ls) and j < len(us):
        if ls[i][0] <= us[j][0]:
            res += ls[i][2]*ls[i][1]
            i+=1
        else:
            res += us[j][2]*us[j][1]
            j+=1
            
    while i < len(ls):
        res += ls[i][2]*ls[i][1]
        i+=1
        
    while j < len(us):
        res += us[j][2]*us[j][1]
        j+=1
        
    return res
 
            
        










s= ["aAa","AaAa","abAAzcacAcbA","aaaaacbb","aacaaBb","aacAabB","Cc","","noiwufeiwnfwjelbieubsaniOERGNEOIVUHAECUANEICBAofaoiehoiashioecs"]
for i in s:
    print(solve(i))