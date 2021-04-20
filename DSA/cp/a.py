import math
n = int(input())



if n%2 == 0:
    i = 2
else:
    i = 1
s = 1
res = []
prod = 1
ind = 0
temp=[]
totake = 0
while s < n:
    prod*=s
    res.append(s)
    if prod%n == 1:
        #print(prod,temp)
       
        totake = ind
    s+=i
    ind+=1
   
print(len(res[:totake+1]))
print(*res[:totake+1])