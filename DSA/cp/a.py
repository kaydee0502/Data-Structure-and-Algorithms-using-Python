def getMinJumps(s):
  
  
    ones = []
  
    jumps, median, ind = 0, 0, 0
  
    
    for i in range(len(s)):
        if(s[i] == '*'):
            ones.append(i)
  
    if(len(ones) == 0):
        return jumps
  
   
    median = ones[len(ones) // 2]
    ind = median
 
    for i in range(ind, -1, -1):
        if(s[i] == '*'):
            jumps += ind - i
            ind -= 1
  
    ind = median
  
   
    for i in range(ind, len(s)):
        if(s[i] == '*'):
            jumps += i - ind
            ind += 1
  

    return jumps


t = int(input())

while t:
    
    t-=1