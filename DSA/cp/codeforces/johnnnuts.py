n,x = map(int,input().split())

an = list(map(int,input().split()))

k = int(input())

kn = list(map(int,input().split()))

s = sum(an)

for i in kn:
    s-=an[i-1] 
    
print(s+1)