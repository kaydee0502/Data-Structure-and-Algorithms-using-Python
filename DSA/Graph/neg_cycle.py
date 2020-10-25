def negative_cycle(adj, cost):
    #write your code here
    dist=[float('inf')]*len(adj)
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
                    if i == len(adj) - 1:
                        return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))