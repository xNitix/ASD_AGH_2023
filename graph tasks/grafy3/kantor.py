# wymiana walut - Dana jest tabela kursów walut. Dla kazdych dwoch walut x oraz y wpis
# K [x][y] oznacza ile trzeba zaplacic waluty x zeby otrzymac jednostke waluty y. Prosze zaproponowac al-
# gorytm, który sprawdza czy istnieje taka waluta z, ze za jednostke z mozna uzyskac wiecej niz jednostke z
# przez serie wymian walut.
# By wyjsc na plus przy zamianach musieli bysmy K[x1][y1]*K[x2][y2]*k[x3][y3]... < 1
# jesli zlogarytmujemy obie strony wychodzi log(K[x1][y1]*K[x2][y2]*k[x3][y3]...) < 0
# a z wlasnosci logarytmu wiemy log(K[x1][y1])+ log(K[x2][y2]) +log(K[x3][y3]) + ... < 0
# Z tego wynika by wyjsc na plus musimy zamienic kursy na logarymty i znalezc ujemny cykl
# Poniewaz bedzie to dowolna waluta Z i mamy postac macierzow to do znalezienia ujemnego 
# kursu uzyje algorytmu Floyda Warshall'a
# Zlozonosc : O(V^3) - Floyd Warshall
from math import log10

def Kantor(G):
    n = len(G)
    G2 = [[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            G2[i][j] = log10(G[i][j])
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G2[j][k] > G2[i][k] + G2[j][i]:
                    G2[j][k] = G2[i][k] + G2[j][i]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if G2[j][k] > G2[i][k] + G2[j][i]:
                    return True
                
    return False
