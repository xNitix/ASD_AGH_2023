# G - graf
# D - poejmnosc
# F - paliwo za 1 litr w danym wierzcholku
from queue import PriorityQueue
def podroznik(G,D,s,t,F):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n*(D+1))]
    parent = [ None for _ in range(n*(D+1))]
    Que = PriorityQueue()
    start_D=0
    wagi[s + start_D * n]=0
    Que.put((wagi[s + start_D * n],start_D,s + start_D * n))
    
    def relax(wagi,u,v,Gas_po_l,waga,F,n):
        if wagi[v + n * Gas_po_l] > wagi[u] + waga * F[u % n]:
            wagi[v + n * Gas_po_l] = wagi[u] + waga * F[u % n]
            return True
        return False
    while not Que.empty():
        _ , bak, u = Que.get()

        for v,waga in G[u % n]:
            if waga <= D:
                for paliwo in range(D+1):
                    if waga <= (bak + paliwo) <= D:
                        Gas_po_l = bak + paliwo - waga
                        if relax(wagi,u,v,Gas_po_l,paliwo,F,n):
                            parent[v + n * Gas_po_l] = u
                            Que.put((wagi[v +  n * Gas_po_l],Gas_po_l,v + n * Gas_po_l))

    path=[]  
    p = parent[t]
    path.append(t%n)
    while p != None:
        path.append(p%n)
        p = parent[p]
    path.reverse()   
    return wagi[t],path

graph =[
    [(1,7),(3,10),(5,30)],
    [(0,7),(3,8),(2,14)],
    [(1,14),(3,9),(4,15)],
    [(0,10),(1,8),(2,9),(4,20),(5,5)],
    [(2,15),(3,20),(5,15)],
    [(0,30),(3,5),(4,15)]
]

F = [20,3,100,5,5,10]

print(podroznik(graph,30,0,5,F))