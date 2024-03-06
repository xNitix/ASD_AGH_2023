# Algorytm Prima do znalezienia MST (minimalne drzewo rospinajace)
# Implementacja dla list sąsiedztwa.
# Zlozonosc : O(E*log(V))

from queue import PriorityQueue
def prim(G):
    inf = float("inf")
    n = len(G)
    visited = [False for _ in range(n)]
    wagi = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    Que = PriorityQueue()
    wagi[0] = 0
    Que.put([wagi[0],0])
    
    while not Que.empty():
        _, u = Que.get()
        visited[u] = True
        for v,edge in G[u]:
            if not visited[v]:
                 if wagi[v] > edge:
                     wagi[v] = edge
                     parent[v] = u
                     Que.put([wagi[v],v])
    
    MST=[]
    for i in range(n):
        if parent[i] != None:
             MST.append([parent[i],i,wagi[i]])
    
    if len(MST) < n - 1:
        return False
    
    return MST