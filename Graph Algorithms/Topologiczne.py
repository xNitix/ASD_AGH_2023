def DFS_sort_topologiczne(G):
    n = len(G)
    time = 0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    res = []
    
    def DFSVisit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        nonlocal res
        
        time +=1
        visited[u]=time
        
        for v in G[u]:
            if visited[v] == False:
                parent[v]=u
                DFSVisit(G,v)
        
        #time += 1        
        res.append(u)
    
    for i in range(len(G)):
        if visited[i] == False:
            DFSVisit(G,i)
    res.reverse()
    return res
        
        