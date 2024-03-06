from queue import PriorityQueue
def podroznik(G,D,F,s,t):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n*(D+1))]
    Que = PriorityQueue()
    star_gaz = 0
    wagi [s + n * star_gaz] = 0
    
    Que.put([wagi[s + n*star_gaz],0,s + n * star_gaz]) # cena | ile w bak | wierzcholek
    
    def relax(u,v,paliwo,bak,km):
        cena_za_tank = paliwo * F[u%n]
        if wagi[v + n*(paliwo + bak - km)] > wagi[u] + cena_za_tank:
            wagi[v + n*(paliwo + bak - km)] = wagi[u] + cena_za_tank 
            return True
        return False
    
    while not Que.empty():
        
        _,bak,u = Que.get()
        
        if u == t:
            return wagi[t]
        
        for v,km in G[u%n]:
            for paliwo in range(0,D + 1 - bak):
                if paliwo + bak - km >= 0:
                    if relax(u,v,paliwo,bak,km):
                        Que.put([wagi[v + n*(paliwo + bak - km)],bak + paliwo - km,v + (paliwo + bak - km)*n])


graph =[
    [(1,7),(3,10),(5,30)],
    [(0,7),(3,8),(2,14)],
    [(1,14),(3,9),(4,15)],
    [(0,10),(1,8),(2,9),(4,20),(5,5)],
    [(2,15),(3,20),(5,15)],
    [(0,30),(3,5),(4,15)]
]

F = [20,3,100,5,5,10]

print(podroznik(graph,30,F,0,5))