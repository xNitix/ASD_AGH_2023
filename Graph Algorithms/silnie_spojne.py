def silnie_spojne(G):
    n = len(G)
    visited = [False for _ in range(n)]
    order = []

    def DFSVisit(G,s,visited,order ):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFSVisit(G,v,visited,order)
        order.append(s)
    
    for i in range(n):
        if not visited[i]:
            DFSVisit(G,i,visited,order)
            
    def Flip_Edge(G):
        n = len(G)
        G_C = [[] for _ in range(n)]
        for i in range(n):
            for v in G[i]:
                G_C[v].append(i)
        return G_C
    
    G2 = Flip_Edge(G)
    
    order.reverse()  
    
    visited = [False for _ in range(n)]
    res = []
    
    for i in order:
        components = []
        if not visited[i]:
            DFSVisit(G2,i,visited,components)
            res.append(components)
            
    # for i in res:
    #     if len(i) == 1:
    #         return False
    
    return res
