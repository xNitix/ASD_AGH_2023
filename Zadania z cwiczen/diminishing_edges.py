# Malejace krawedzie - Dany jest graf G = (V. E). gdzie kazda krawedz ma wage ze zbiorn {L…... (E]) (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, kóry da danych 
# wierzcholków x i y sprawdza, czy istnieje Sciezka z x do y w ktorej przechodzimy po krawedziach o coraz mniejszych wagach.
# Modyfikujemy DFSVisit tak by mogl wchodzic do krawedzi w ktorych juz byl, jednak by z kazdym razem wybieral tylko mniejsze wagi na krawdziach
# zlozonosc taka O(V^2)

def DFSVisit(G,s,t):
    n = len(G)
    visited=[False for _ in range(n)]
    
    def DFSVisit(G,s,t,visited,waga):
        visited[s]=True
        for v,wag in G[s]:
            if wag < waga:
                print(v)
                DFSVisit(G,v,t,visited,wag)
    inf = float("inf")
    DFSVisit(G,s,t,visited,inf)
    return visited[t]
            

graph = {
    0: [(1, 2), (2, 3), (3, 1)],
    1: [(0, 2), (2, 4), (4, 5)],
    2: [(0, 3), (1, 4), (3, 2), (4, 1)],
    3: [(0, 1), (2, 2), (4, 4), (5, 3)],
    4: [(1, 5), (2, 1), (3, 4), (5, 2)],
    5: [(3, 3), (4, 2)]
}
print(DFSVisit(graph,0,4))
