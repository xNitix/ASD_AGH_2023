# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych miast 
# i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci (x, y, c), 
# gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.
# wykonujemy dijkstree tylko ze jako wagi do kolejki piorytetowej wkladamy najwieszksze waskie gardlo jakie znajudje
# sie na drodze z ktorej dotarlismy do wierzcholka, w tenm sposob znajdziemy sciezkie z najwiekszym najmniejszym
# gardlem a ilosc grup bedzie rowna k / najwieksze waskie gardlo
# Zlozonosc : O(E*log(v)) - Dijkstra dla reprezentacji listowej
from queue import PriorityQueue

def travel(E,s,t,k):
    n = len(E)
    
    def make_graph(E):
        inf = float("inf")
        n = -inf
        for x,y,c in E:
            n = max(n,x,y)
        n+=1
        G = [[]for _ in range(n)]
        for x,y,c in E:
            G[x].append([c,y])
            G[y].append([c,x])
        return G
            
    def relax(u,v,waga,wagi):
        if wagi[v] < waga:
            wagi[v] = waga
            return True
        return False
    
    G = make_graph(E)
    Que = PriorityQueue()
    inf = float("inf")
    wagi = [-inf for _ in range(n)]
    parents = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    Que.put([wagi[s],s])
    while Que.qsize() != 0:
        us,u = Que.get()
        visited[u] = True
        for edge,v in G[u]:
            if relax(u,v,edge,wagi):
                parents[v] = u
                Que.put([-wagi[v],v])
    return wagi[t]/k
    

