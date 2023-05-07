# Uniwersalne ujscie - Mówimy, ze wierzcholek t w grafie skierowanym jest uniwersalnymujsciem, jesli (a) dla kazdego innego wierzcholka istnieje krawedz z v do t, oraz
# (b) nie istnieje zadna krawedz wychodzaca z t. Podaj algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej.
# Przechodze po macierzy grafu w taki sposob ze gdy napotkam 0 to przesuwam sie o kolejna kolumne ( w prawo ), a gdy spotkam 1 to przechodze jeden wiersz nizej ( w dol )
# Dlaczego ? by wierzcholek byl uniwersalnym wyjsciem musi miec w wierszu same 0 ( nie ma krawedzi do zadnego innego wierzhcolka ), oraz w kolumnie n-1 jedynek, (wchodza do niego
# wszytskie pozostale wierzcholki)
# Zlozonosc : O(V)

def universal_sink(G):
    n = len(G)
    w = 0 #wiersz
    k = 0 #kolumna
    while w < n and k < n:
        if G[w][k] == 0:
            k+=1
        else:
            w+=1
            
    if w == n:
        return None
    
    for i in range(n):
        if G[w][i] == 1:
            return None
        if G[i][w] == 0 and w != i:
            return None
    
    return w
