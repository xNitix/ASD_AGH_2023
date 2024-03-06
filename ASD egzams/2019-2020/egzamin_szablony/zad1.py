from zad1testy import runtests
from queue import PriorityQueue


def islands(G, A, B):
    inf = float("inf")
    n = len(G)
    Que = PriorityQueue()
    isl = [inf for _ in range(3*n)]
    isl[A] = 0
    isl[A+n] = 0
    isl[A+2*n] = 0
    Que.put([0,A,0])
    
    def relax(isl,v,u,tran,price):
        if isl[v + tran] > isl[u] + price:
            isl[v + tran] = isl[u] + price
            return True
        return False
    
    while not Que.empty():
        sum,u,transport = Que.get()
        
        if B == u%n:
            return sum
        
        for v in range(len(G)):
            cost = G[u%n][v]
            if cost != 0:
                if cost == 1 and transport != 1:
                    if relax(isl,v,u,0,cost):
                        Que.put([isl[v + 0],v + 0, 1])
                if cost == 5 and transport != 5:
                    if relax(isl,v,u,n,cost):
                        Que.put([isl[v + n],v + n, 5])
                if cost == 8 and transport != 8:
                    if relax(isl,v,u,2*n,cost):
                        Que.put([isl[v + 2*n],v + 2*n, 8])
    
    return isl

runtests( islands ) 

