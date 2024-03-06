from queue import PriorityQueue

def dijkstra(G,i,j):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n)]
    Que = PriorityQueue()
    
    wagi[i] = 0
    Que.put([0,i])
    
    def relax(u,v,waga):
        if wagi[v] > wagi[u] + waga:
            wagi[v] = wagi[u] + waga
            return True
        return False
            
    
    while not Que.empty():
        _,u = Que.get()
        
        if u == j:
            return wagi[j]
        
        for v,waga in G[u]:
            if relax(u,v,waga):
                Que.put([wagi[v],v])
    
    return None
    

def winda(T,i,j):
    n = len(T)
    G = [[]for _ in range(101)]
    for k in range(n):
        T[k][0].sort()
    for k in range(n):
        for m in range(len(T[k][0])-1):
            G[T[k][0][m]].append([T[k][0][m+1],T[k][1]*(T[k][0][m+1]-T[k][0][m])])
    
    return dijkstra(G,i,j)
    
    
    
T = [[[1,3,4],3],[[3,5,2,4],1],[[2,3,1],2]]

print(winda(T,1,5))