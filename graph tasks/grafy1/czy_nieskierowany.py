# Czy nieskierowany - Prosze podac algorytm, który majac na wejsciu graf G reprezentowany
# przez listy sasiedztwa sprawdza, czy jest nieskierowany (czyli czy dla kazdej krawedzie u -
# v istnieje takze krawed przeciwna).
# Tworzymy macierz krawedzi, jesli przechodzimy przez krawedz za (v-u) to zaznaczamy to w macierzy
# i sprawdzmy czy zaznaczylismy wczesniej krawedz (u-v) jesli tak od licznka odejmujemy 1, a jesli
# nie to dodajemy, jesli licznik na koncu bedzie wynoisl 0 to jest to graf nieskierowany, jesli > 0
# to skierowany
# Zlozonosc : O(V^2) - tworzenie macierzy i przejscie po calym grafie

def is_directed(G):
    n = len(G)
    edges = [[False for _ in range(n)]for _ in range(n)]
    counter = 0
    for i in range(n):
        for v in G[i]:
            if not edges[i][v]:
                if not edges[v][i]:
                    edges[i][v] = True
                    counter+=1
                elif edges[v][i]:
                    edges[i][v] = True
                    counter-=1
    return counter == 0

G = [[1,2],
     [0,3],
     [0,3],
     [1,2,4],
     [3]]

print (is_directed(G))