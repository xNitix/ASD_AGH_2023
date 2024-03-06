def make_graph(E):
    n = len(E)
    inf = float("inf")
    max_val = -inf
    min_val = inf
    
    for i in range(n):
        for j in range(2):
            max_val = max(max_val,E[i][j])
            min_val = min(min_val,E[i][j])
            
    graph = [[] for _ in range(max_val-min_val + 1)]
    
    for i in range(n):
        graph[E[i][0]-min_val].append(E[i][1]-min_val)
        graph[E[i][1]-min_val].append(E[i][0]-min_val)

    return graph,min_val
    

def setcion(E,a,b):
    graph,min_val = make_graph(E)
    visited = [False for _ in range(len(graph))]
    def DFS(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS(G,v)
                
    DFS(graph,a-min_val)
    
    return graph,visited
    
E = [(1,3),(2,5),(3,4),(1,2),(7,9)]

print(setcion(E,2,7))