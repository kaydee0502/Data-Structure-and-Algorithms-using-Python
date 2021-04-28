

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
                    
    






m = "abxabcabcaby"
p = "abbcbbccaaaaaabcbbaccccaabbcbbccaa"
print(kmp_table(p))