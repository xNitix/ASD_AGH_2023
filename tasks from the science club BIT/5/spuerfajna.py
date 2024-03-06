from queue import PriorityQueue
def super_fajne(G,s):
    n = len(G)
    inf = float("inf")
    cost = [[inf,inf]for _ in range(n)]
    Que = PriorityQueue()
    cost[s]=[0,0]
    
    Que.put([cost[s],s])
    
    def relax(u,v,edge):
        if cost[v][0] > cost[u][0] + edge :
            cost[v][0] = cost[u][0] + edge
            cost[v][1] = cost[u][1] + 1
            return True
        return False
    
    while not Que.empty():
        [waga,odl],u = Que.get()
        
        for edge,v in G[u]:
            if relax(u,v,edge):
                Que.put([cost[v],v])
                
    return cost

G = [[[1,1],[3,2]],
     [[1,0],[2,4]],
     [[3,0],[4,3]],
     [[4,2],[4,4]],
     [[2,1],[2,5],[4,3]],
     [[2,4]]
]

print(super_fajne(G,0))