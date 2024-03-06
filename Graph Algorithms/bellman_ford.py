# Bellman-Ford - znajduje najkrotsza sciezke najkrótsze ścieżki z pojedynczego wierzchołka źródłowego do wszystkich innych wierzchołków 
# wliczajac w to ujemkne wagi, dijkstra nie wroci juz nigdy do punktu w ktorym byl, Bellman sprawdza kazda mozliwa odleglosc miedzy kazda para,
# wiec zawsze wroci odpowiddnia sciezke, nawet gdy np musimy isc po malejacych krawedziach, jesli po potrojnnym for
# wykonamy jeszcze raz proces relakasacji krawedzi i droga sie poprawki to oznacza ze mamy ujemny cykl
# Zlozonosc : O(V*E)

def Bellman_Ford(G,s):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n)]
    parents = [None for _ in range(n)]
    wagi[s] = 0
    
    def relax(u,v,wagi,edge):
        if wagi[v] > wagi[u] + edge:
            wagi[v] = wagi[u] + edge
            return True
        return False
    
    for _ in range(n-1):
        for u in range(n):
            for edge,v in G[u]:
                if relax(u,v,wagi,edge):
                    parents[v] = u
    # sprawdzanie czy ujemny cykl
    for u in range(n):
        for edge,v in G[u]:
            if relax(u,v,wagi,edge):
                return None
    
    return wagi,s