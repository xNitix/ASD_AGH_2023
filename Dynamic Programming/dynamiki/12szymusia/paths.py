from queue import PriorityQueue
def paths (G,s,t): 
    n = len(G)
    
    def Dijksra(G,s,t,parents):
        n = len(G)
        inf=float("inf")
        Que=PriorityQueue()
        wagi=[inf for _ in range(n)]

        wagi[s] = 0
        Que.put((0,s))
        
        while Que.qsize() != 0:
            nic,v = Que.get()
            for u,waga in G[v]:
                if wagi[v] + waga <= wagi[u]:
                    wagi[u] = wagi[v] + waga
                    parents[u].append(v) 
                    Que.put((wagi[u],u))
        return wagi[t]
    
    def DFS(G,t):
        n = len(G)
        visited = [False for _ in range(n)]
        counter = 0
        
        def DFS_visit(G,u,visited):
            nonlocal counter
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    DFS_visit(G,v,visited)
                    
                counter += 1
                
        DFS_visit(G,t,visited)
        return counter
    
    parents = [[] for _ in range(n)]
    Dijksra(G,s,t,parents)
    return DFS(parents,t)


    
    
G = [[(1,2), [2,4]],
      [(0,2), (3, 11), (4,3)],
      [(0,4), (3,13)],
      [(1,11), (2,13), (5, 17), (6,1)],
      [(1,3), (5,5)],
      [(3,17), (4,5), (7,7)],
      [(3,1), (7,3)],
      [(5,7), (6,3)]]
s = 0
t = 7

print(paths(G,s,t))