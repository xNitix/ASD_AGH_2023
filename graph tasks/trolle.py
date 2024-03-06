def trolle(G,C):
    n = len(C)
    graph = [[]for _ in range(n)]
    
    for i in range(len(G)):
        u,v = G[i]
        graph[v].append(u)
        graph[u].append(v)
    
    def bridge(G):
        n = len(G)
        inf = float("inf")
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

        for i in range(n):
            if visited[i] == False:
                DFS(G,i,visited,parent_t,time_vis,low,time)
        
        return time_vis,low,parent_t
        
    time_vis,low,parents = bridge(graph)
    
    visited = [False for _ in range(n)]
    def DFSVisit(G,u):
        visited[u]=True
        res = C[u]
        for v in G[u]:
            if visited[v] == False:
                res += DFSVisit(G,v)
        return res
    
    def DFS(G,u):
        visited[u] = True
        res = 0
        x = 0
        y = 0
        
        for v in G[u]:
            if not visited[v]:
                if time_vis[v] == low[v] and parents[v] != None:
                    val = DFSVisit(G,v)
                    if val > res:
                        res = val
                        x = u
                        y = v 
                else:
                    val,x1,y1 = DFS(G,v)
                    if res < val:
                        res = val
                        x = x1
                        y = y1
   
        return [res,x,y]
    wyn,a,b = DFS(graph,0)
    return "wynik : ",wyn," most : ",[a,b]



E = [(0, 1), (1, 2), (1, 3), (3, 0), (3, 4), (4, 8), (8, 5), (4, 6), (6, 8), (7, 6)]
C = [0, 2, 7, 13, 5, 2, 3, 1, 5]

print(trolle(E,C))