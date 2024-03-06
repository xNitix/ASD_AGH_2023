from zad1testy import runtests
from queue import Queue
from math import ceil

def best_root( L ):
    n = len(L)
    visited = [False for _ in range(n)]
    visited[0] = 1

    Que = Queue()
    
    Que.put(0)
    
    # szukam jedno z koncow srednicy
    while not Que.empty():
        u = Que.get()
        for v in L[u]:
            if not visited[v]:
                Que.put(v)
                visited[v] = visited[u] + 1
                
    start = max(visited)
    indx = visited.index(start)
    
    visited = [False for _ in range(n)]
    visited[indx] = 1
    Que.put(indx)
    
    # z konca srednicy puszczam bst by dowiedziec sie jaka ma dlugosc
    while not Que.empty():
        u = Que.get()
        for v in L[u]:
            if not visited[v]:
                Que.put(v)
                visited[v] = visited[u] + 1
                
    diameter_len2 = max(visited)
    diameter_len = ceil(diameter_len2/2)
    
    visited2 = [False for _ in range(n)]
    visited2[indx] = 1
    Que.put(indx)
    last_good = 0
    res = 0
    
    # wynikiem bedzie jeden z wierzcholkow ktory bedzie w polowie srednicy 
    def DFS_visit(u,graph,visited,visited2,stp,diameter_len):
        nonlocal last_good
        nonlocal res
        if visited[u] == diameter_len:
            res = last_good

        visited2[u] = True
        for v in graph[u]:
            if not visited2[v]:
                if visited[v] == stp:
                    last_good = v
                DFS_visit(v,graph,visited,visited2,stp,diameter_len)

    DFS_visit(indx,L,visited,visited2,diameter_len,diameter_len2)
    
    return res


runtests( best_root ) 
