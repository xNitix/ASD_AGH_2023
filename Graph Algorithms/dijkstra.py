# Dijkstra macierzowa O (V^2)
from math import inf
def Dijkstra_m(G,s,k):
    n = len(G)
    wagi=[inf for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    
    wagi[s]=0
    
    while True:
        minimum=inf
        min_indx=0
        
        for i in range(n):
            if visited[i] == False:
                if wagi[i] < minimum:
                    minimum=wagi[i]
                    min_indx=i
                    
        if minimum == inf:
            break
        
        visited[min_indx]=True
        
        for u in range(len(G[min_indx])):
            if G[min_indx][u] == -1 or visited[u] == True:
                continue
            if wagi[min_indx] + G[min_indx][u] < wagi[u]:
                wagi[u]=wagi[min_indx] + G[min_indx][u]
                parent[u]=min_indx
                
    return wagi[k]

# Dijkstra Lista sąsiedztwa (E*log(V))

from queue import PriorityQueue
def Dijksra_L(G,s,t):
    n = len(G)
    inf=float("inf")
    Que=PriorityQueue()
    wagi=[inf for _ in range(n)]
    parent=[None for _ in range(n)]
    wagi[s] = 0
    Que.put((0,s))
    
    while Que.qsize() != 0:
        nic,v = Que.get()
        for u,waga in G[v]:
            if wagi[v] + waga < wagi[u]:
                wagi[u] = wagi[v] + waga
                parent[u] = v
                Que.put((wagi[u],u))
    return wagi[t]
