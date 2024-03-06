def DFS(G):
    n = len(G)
    time = 0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    
    def DFSVisit(G,u):
        nonlocal time
        time +=1
        visited[u]=time
        for v in G[u]:
            if visited[v] == False:
                parent[v]=u
                DFSVisit(G,v)
    
    for i in range(len(G)):
        if visited[i] == False:
            DFSVisit(G,i)
    
            