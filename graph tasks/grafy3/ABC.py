from math import inf
def bridge(G):
    n = len(G)
    visited=[False for _ in range(n)]
    parent_t=[None for _ in range(n)]
    time_vis=[0 for _ in range(n)]
    low = [inf for _ in range(n)]
    time = 0

    def DFS(G,parent,visited,parent_t,time_vis,low,time):
        visited[parent] = True
        time_vis[parent]=time
        time+=1
        low[parent]=time_vis[parent]
        for v in G[parent]:
            if visited[v] == False:
                parent_t[v]=parent
                DFS(G,v,visited,parent_t,time_vis,low,time)
                low[parent]=min(low[parent],low[v])
            elif parent_t[parent] != v:
                low[parent]=min(low[parent],time_vis[v])

    bridges = []
    for i in range(n):
        if visited[i] == False:
            DFS(G,i,visited,parent_t,time_vis,low,time)
    for i in range(n):
        if time_vis[i] == low[i] and parent_t[i] != None:
            bridges.append([parent_t[i],i])
    return bridges
graph = [
    [1, 2],
    [0, 2],
    [0, 1, 6],
    [5, 4],
    [5, 3],
    [3,4,6],
    [2,7,5],
    [6]
    ]

print(bridge(graph))