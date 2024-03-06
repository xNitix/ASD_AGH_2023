# Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci macierzowej
# (domknięcie przechodnie grafu G, to graf nad tym samym zbiorem wierzchołków, który dla każdych dwóch 
# wierzchołków u i v ma krawędź z u do v wtedy i tylko wtedy, gdy w G istnieje ścieżka z u do v.
# Robimy kopie grafu z zachowaniem isteniejacych krawedzi, nastepnie puszczamy algorytm Floyda_Warshall'a
# Zlozonosc : O(V^3) - Floyd_Warshall

def domknięcie(G):
    n = len(G)
    G2 = [[False for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                G2[i][j] = True
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if not G2[i][j]:
                    G2[j][k] = G2[j][i] and G2[i][k]
                    
    return G2