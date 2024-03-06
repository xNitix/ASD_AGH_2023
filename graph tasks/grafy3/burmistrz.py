from queue import PriorityQueue
from math import ceil
def autostrady(E):
    n = len(E)
    inf = float("inf")
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                xi,yi = E[i]
                xj,yj = E[j]
                G[i].append([j,((xi-xj)**2 + (yi-yj)**2)**(1/2)])
     
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
            return -1
        
        return MST
    
    edges = prim(G)
    if edges == -1:
        return None 
    edges.sort(key=lambda x: x[2])
    
    res = ceil(edges[len(edges)-1][2]) - ceil(edges[0][2])
    i = 0
    while True:
        u,v,waga = edges[i]
        G[u].remove([v,waga])
        G[v].remove([u,waga])
        edges2 = prim(G)
        if edges2 == -1:
            return res
        else:
            res = min(res,ceil(edges2[len(edges)-1][2]) - ceil(edges2[0][2]))
        i+=1
    

E = [(10,10),(15,25),(20,20),(30,40)]

print(autostrady(E))


# [[[1, 15.811388300841896], [2, 14.142135623730951], [3, 36.05551275463989]],
#  [[0, 15.811388300841896], [2, 7.0710678118654755], [3, 21.213203435596427]],
#  [[0, 14.142135623730951], [1, 7.0710678118654755], [3, 22.360679774997898]],
#  [[0, 36.05551275463989], [1, 21.213203435596427], [2, 22.360679774997898]]]