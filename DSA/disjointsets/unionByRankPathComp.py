

def find(x):
    if x == parent[x]:
        return x
    
    # path compression
    parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a_p = find(a)
    b_p = find(b)
    
    if rank[a_p] < rank[b_p]:
        parent[a_p] = b_p
    elif rank[a_p] > rank[b_p]:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p
        rank[b_p] += 1




n = 7
task = [(1,2),(2,3),(4,5),(6,7),(5,6),(3,7)]
parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

print(parent)

for i,j in task:
    union(i,j)
    print(parent)
    print("r",rank)
    
for i in range(1,n+1):
    a = find(i)
    print("comp",parent)

