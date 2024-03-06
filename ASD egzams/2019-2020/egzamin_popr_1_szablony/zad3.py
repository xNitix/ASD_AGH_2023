from zad3testy import runtests

def make_graph(Tab):
    n = len(Tab)
    graph = [[]for _ in range(n)]
    
    for u in range(n):
        for v in range(n):
            if Tab[u][v] == 1:
                graph[u].append(v)
    
    return graph


def topological_sort(graph):
    
    def DFS_visit(u,graph,visited,res):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                DFS_visit(v,graph,visited,res)
                
        res.append(u)
    
    n = len(graph)
    visited = [False for _ in range(n)]    
    res = []
    
    for u in range(n):
        if not visited[u]:
            DFS_visit(u,graph,visited,res)
            
    res.reverse()
    return res
            
        
    
def tasks(T):
    graph = make_graph(T)
    x = topological_sort(graph)
    return x
    



runtests( tasks )
