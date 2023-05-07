# Cykl na cztery - Dany jest graf nieskierowany G zawierajacy n wierzcholkow. Zaproponuj algorytm, który stwierdza czy w G istnieje cykl skladajacy sie z dokladnie 4 wierzcholkow.
# Zakladamy, że graf reprezentowany jest prez macierz sasiedztwa A.
# przechodzimy po wszytskich parach wierzcholkow i szukamy czy sa oni obaj
# polaczeni z dwoma innymi wierzcholkami co da nam cykl dlugosci 4
# Zlozonosc : O(V^3)

def find_C4(G):
    n = len(G)
    for u in range(1,n): # przedzialy for'ow sa zmienieone tak by u != v, gdyz gdyby tak sie 
        for v in range(u): # staolo szukali bymy czy jeden i ten sam wierzcholek na dwoch sasiadow
            z = False
            for i in range(n):
                if G[u][i] and G[v][i]:
                    if z: return (u, v, z, i)
                    z = i
    return ()

#   0 1 2 3 4 5 6 7 
G=[[0,1,1,0,0,0,0,0], #0
   [1,0,0,0,1,0,0,0], #1
   [1,0,0,1,0,1,0,0], #2
   [0,0,1,0,1,0,0,0], #3
   [0,1,0,1,0,1,0,0], #4
   [0,0,1,0,1,0,1,0], #5
   [0,0,0,0,0,1,0,1], #6
   [0,0,0,0,0,0,1,0]] #7

print(find_C4(G))
