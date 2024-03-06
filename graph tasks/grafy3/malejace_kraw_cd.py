# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne).
# Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag,
# która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).
# Graf jest reprezentowany jako tablica wypełniona 3-elementowymi tablicami: [u,v,edge].
# u,v-wierzcholki, edge - wartość krawędzi pomiędzy nimi
# Sortujemy krawedzie malejaco, w ten sposob bedziemy szli tylko po malejacych krawedziach

def malejące(G,s,t):
    n = len(G)
    inf  = float("inf")
    wagi = [inf for _ in range(n)]
    parents = [None for _ in range(n)]
    G.sort(key = lambda x:x[2],reverse = True)
    wagi[s] = 0
    
    def relax(u,v,wagi,edge):
        if wagi[v] > wagi[u] + edge:
            wagi[v] = wagi[u] + edge
            return True
        return False
    
    
    for u,v,edge in G:
        if relax(u,v,wagi,edge):
            parents[v] = u
    
    if wagi[t] == inf:
        return inf
    
    patch = []
    patch.append(t)
    p = parents[t]
    while p != None:
        patch.append(p)
        p = parents[p]
    patch.reverse
    
    return wagi[t],patch


G = [[0,2,13],[0,1,9],[1,3,6],[2,3,12],[2,4,14],[3,4,11],[1,4,10]]

print(malejące(G,0,4))
                    