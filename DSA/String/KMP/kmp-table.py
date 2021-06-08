def lps(s):
	    
        if not s:
            return 0
        if len(s) == 1:
            1
            
            
        kmp = [0]*len(s)
        i = 1
        j = 0
	   
	   
        while i < len(s):
            if s[i] == s[j]:
                kmp[i] = j + 1
                i+=1
                j+=1
                
            else:
                while j != 0:
                    if s[j] == s[i]:
                        break
                    
                    j = kmp[j-1]
                        
                if j == 0 and s[j] != s[i]:
                    i+=1
                else:
                    kmp[i] = j+1
                    
        print(kmp)
        return kmp[-1]

def kmp_table(pat):
    if not pat:
        return []
        
    if len(pat) == 1:
        return [0]
    
    table = [0] * len(pat)
    
    j = 0
    i = 1
    
    
    while i < len(pat):
        
        if pat[i] == pat[j]:
            table[i] = j + 1
            i+=1
            j+=1
            
        else:
           
            while not(j == 0 or pat[i] == pat[j]):
                print(i,j)
                j = table[j-1]
              
           
            if j != 0 or pat[i] == pat[j]:
                table[i] = j+1
            else:
                i+=1
                
        
                
    return table
                    
    






m = "joeuljjo"
p = "abyabcd"
print(kmp_table(m))
print(lps(m))