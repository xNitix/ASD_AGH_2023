# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi łączące miasta.
# Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) 
# autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę 
# oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów.
from queue import PriorityQueue

def Ala_Bob(G,x,y):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n*2)]
    parents = [None for _ in range(n*2)]
    Que = PriorityQueue()
    wagi[x] = 0
    wagi[x + n] = 0
    
    Que.put([0,'A',x])
    Que.put([0,'B',x+n])
    
    def relax(u,v,wagi,who,edge):
        if wagi[v + who] > wagi[u] + edge:
            wagi[v + who] = wagi[u] + edge
            return True
        return False
    
    while not Que.empty():
        _,who,u = Que.get()
        for edge,v in G[u%n]:
            if who == 'A':
                if relax(u,v,wagi,n,0):
                    parents[v + n] = u
                    Que.put([wagi[v+n],'B',v+n])
            if who == 'B':
                if relax(u,v,wagi,0,edge):
                    parents[v] = u
                    Que.put([wagi[v],'A',v])
    mini = 0
    if wagi[y] > wagi[y+n]:
        mini = y+n
    else:
        mini = y
    patch=[]
    patch.append(mini%n)
    par = parents[mini]
    while par != None:
        patch.append(par%n)
        if parents[par] == None:
            if par >= n:
                who = "Ala"
            else:
                who = "Bob"         
        par = parents[par]

    patch.reverse()
    return (wagi[mini],who,patch)

G = [[[10,1],[50,3],[200,6]],
     [[10,0],[10,3]],
     [[10,3],[30,4]],
     [[10,1],[50,0],[10,2]],
     [[30,2],[40,5]],
     [[200,6],[40,4]],
     [[200,5],[200,0]]] 

x,y,z = Ala_Bob(G,0,5)
print("ile przejchała Ala : ",x,"km")
print("Kto zaczyna : ",y)
print("trasa : ",z)