# Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny
# Liczby bierzemy jako logarymty dzieki temu wiemy ze z wlasnosci logarytmow 
# Log(a) + log(b) = log(a*b) w ten sposob bedziemy mieli logarytm z iloczymu 
# kolejnych wag i dzieku temu mozemy uzyc juz zwyklego dijkstry by znalezc najmejszy logarytm
# Zlozonosc  : O(E * log(v)) - dijkstra reprezentacja listowa 
from queue import PriorityQueue
from math import log10

def Log(G,v,u):
    n = len(G)
    inf  = float("inf")
    Que = PriorityQueue()
    wagi = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    wagi[v]=0
    Que.put([wagi[v],v])
    while Que.qsize() != 0:
        _,t = Que.get()
        if t == u:
            break
        for v,waga in G[t]:
            if wagi[t] + log10(waga) < wagi[v]:
                wagi[v] = wagi[t] + log10(waga)
                parent[v] = t
                Que.put([wagi[v],v])
    par = parent[u]
    print(u)
    while par != None:
        print(par)
        par = parent[par]
        