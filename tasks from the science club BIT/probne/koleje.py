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

def koleje ( T ):
    n = len(T)
    maxi = -float("inf")
    for i in range(n):
        a = T[i][0]
        b = T[i][1]
        maxi = max(maxi,a,b)
        if T[i][0] > T[i][1]:
            a = T[i][0]
            b = T[i][1]
            T[i] = (b,a)
    T.sort(key=lambda x:x[1])
    T.sort(key=lambda x:x[0])
    
    edges = [[]for _ in range(maxi+1)]
    edges[T[0][0]].append(T[0][1])
    edges[T[0][1]].append(T[0][0])
    for i in range(1,n):
        if T[i] != T[i-1]:
            edges[T[i][0]].append(T[i][1])
            edges[T[i][1]].append(T[i][0])
    
    mosty =  bridge(edges)
    res=[inf for _ in range(n)]
    for i in range(len(mosty)):
        if len(edges[mosty[i][0]]) > 1:
            res[mosty[i][0]] = 1
        if len(edges[mosty[i][1]]) > 1:
            res[mosty[i][1]] = 1
            
    res2 = 0
    for i in range(n):
        if res[i] != inf:
            res2+=1
    return res2
        

        

B = [(3,1),(0,1),(4,2),(1,2),(0,1),(2,4),(2,4),(0,3),(2,4),(1,0),(2,1)]

print(koleje(B))
    