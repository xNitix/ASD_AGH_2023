# Algorytm Floyda-Warschalla
# Znajduje wszystkie najkrótsze ścieżki pomiedzy każdą parą wierzchołków w grafie ważonym.( z dowlnego punktu do dowolnego wierzcholka)
# Wagi krawędzi mogą być zarówno dodatnie jak i ujemne, ale graf nie może posiadać ujemnych cykli.
# Złożoność: O(V^3)

def Floyd_Warschall(G):
    n = len(G)
    inf = float("inf")
    wagi = G[:]
    parents = [[None for _ in range(n)]for _ in range(n)]
    
    def relax(i,j,k,wagi):
        if wagi[j][k] > wagi[j][i] + wagi[i][k]:
            wagi[j][k] = wagi[j][i] + wagi[i][k]
            return True
        return False
    
    
    for i in range(n):
        for j in range(n):# startowy
            for k in range(n): # koncowy
                if relax(i,j,k,wagi):
                    parents[j][k] = i
                    
    # sprawdzanie ujemnego cyklu
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if relax(i,j,k,wagi):
                    wagi[j][k] = -inf
                    parents[j][k] = -1
    
    return wagi,parents