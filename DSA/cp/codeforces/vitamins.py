n = int(input())

def missins(duo):
    pres = {"A","B","C"}
    for i in duo:
        pres.discard(i)
        
    return list(pres)[0]



vits = []
for i in range(n):
    vits.append(input().split())
    
l = ["A","B","C","all"]

d = {x:float("inf") for x in l}

duos = {}

for i,j in vits:
    i = int(i)
    if len(j) == 1:
        d[j] = min(d[j],i)
        
    elif len(j) == 3:
        d["all"] = min(d["all"],i)
        
    else:
        if j in duos:
            duos[j] = min(duos[j],i)
        else:
            duos[j] = i
            
dl = list(duos.keys())
s = 0
for i in "ABC":
    s += d[i]
d["all"] = min(d["all"],s)
#print(d)

for i in range(len(dl)):
    miss = missins(dl[i])
    d["all"] = min(d["all"],d[miss]+duos[dl[i]])
    for j in range(i+1,len(dl)):
        if miss in dl[j]:
            d["all"] = min(d["all"],duos[dl[i]]+duos[dl[j]])
            
if d["all"] == float("inf"):
    print(-1)
else:
    print(d["all"])
        
        
    