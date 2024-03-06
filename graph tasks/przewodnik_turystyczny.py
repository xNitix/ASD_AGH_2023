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
    
C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]       
        
print(travel(C,0,7,100))

