from queue import PriorityQueue

def min_weight_cycle_un_dir(G):
    n = len(G)
    inf = float("inf")
    
    def Dijkstra(G,s,t):
        inf = float("inf")
        n = len(G)
        visited = [False for _ in range(n)]
        cost = [inf for _ in range(n)]
        Que = PriorityQueue()
        
        cost[s] = 0
        Que.put([cost[s],s])
        
        def relax(u,v,edge):
            if cost[v] > cost[u] + edge:
                cost[v] = cost[u] + edge
                return True
            return False
        
        while not Que.empty():
            _,u = Que.get()
            
            if u == t:
                return cost[t]
            
            visited[u]
            for v,edge in G[u]:
                if not visited[v]:
                    if relax(u,v,edge):
                        Que.put([cost[v],v])
                        
        return inf
    
    mini = inf
    
    for i in range(n):
        for j in range(len(G[i])):
            u = i
            v,edge = G[i][j]
            G[i][j] = [v,inf]
            cycle = Dijkstra(G,u,v) + edge
            mini = min(mini,cycle)
            G[i][j] = [v,edge]

    return mini   

  

G = [[[1,2]],
     [[2,3],[0,2]],
     [[3,1],[4,4],[5,2],[1,3]],
     [[2,1],[4,1]],
     [[3,1],[2,4]],
     [[2,2],[6,3],[9,2]],
     [[5,3],[7,1],[8,7]],
     [[6,1],[8,2]],
     [[6,7],[7,2]],
     [[5,2],[10,2]],
     [[9,2],[11,2],[12,3]],
     [[10,2],[12,4]],
     [[11,4],[10,3]]
]

print(min_weight_cycle_un_dir(G))  

# dla skierowanego wystarczy zrobic floyda worsahala i sprawedzic ktore najmiejsze min(dist(u+v)+dist(v+u))  

