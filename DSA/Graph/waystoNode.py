from collections import defaultdict

def DFSutil(S,D,graph,vis):
    vis[S]=True
    global count
    
    if S==D:
        count+=1
    for i in graph[S]:
        #print(i,D)
        
        if not vis[i]:
            print(vis)
            DFSutil(i,D,graph,vis)
    vis[S] = False



def DFS(S,D,graph,verts):
    visits = [False]*verts
    return DFSutil(S,D,graph,visits)
    
        
    
count = 0



T = int(input())
while T:
    count = 0
    V,E = map(int,input().split())
    pre = tuple(map(int,input().split()))
    graph = defaultdict(list)
    for i in range(0,len(pre),2):
        graph[pre[i]].append(pre[i+1])
        
    s,d = map(int,input().split())
        
    DFS(s,d,graph,V)
    print(count)
    T-=1