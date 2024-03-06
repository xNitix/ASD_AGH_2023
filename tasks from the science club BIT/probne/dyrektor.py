def DFS_Euler(G,vertex,res):
    for i in range(len(G)):
        if G[vertex][i] == 1:
            G[vertex][i] = 0
            DFS_Euler(G, i, res)
    res.append(vertex)

def DFS_Euler_path(G):
    # sprawdzam czy istnieje cykl eulera
    for i in range(len(G)):
        edges = 0
        for j in range(len(G[i])):
            if G[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return False
    
    res = [] 
    DFS_Euler(G,0,res)
    res.reverse()
    return res

def dyrektor(G,R):
    n = len(G)
    graph = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            graph[i][G[i][j]] = 1
    for i in range(n):
        for j in range(len(R[i])):
            graph[i][R[i][j]] = 0
    return DFS_Euler_path(graph)
    
    
    