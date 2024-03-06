def DFS_Euler(G,vertex,res):
    for i in range(len(G)):
        if G[vertex][i] == 1:
            G[vertex][i] = 0
            G[i][vertex] = 0
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