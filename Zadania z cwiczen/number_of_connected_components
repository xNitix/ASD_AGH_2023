# The number of connected_components
# Spójna składowa grafu nieskierowanego G – spójny podgraf grafu G nie zawarty w większym podgrafie spójnym grafu G. Innymi słowy spójna składowa grafu jest to taki
# podgraf, który można ‘wydzielić’ z całego grafu bez usuwania krawędzi. Graf spójny ma jedną spójna składową. Dla przykładu, w lesie spójnymi składowymi są drzewa
# Algorytm : Wykonujemy DFS w grafie G, sprawdzamy czy są jakies nie odwidzone wierzcholki, jesli tak to liczbe skldawodych zwiekszamy i wykonujemy DFS na tym wierzcholku
# Złożonosć : O(V+E) złozonosc DFS 

def CCC(G): 
    n = len(G)
    visited=[False for _ in range(n)]
    Counter=1
    
    def DFS(G,v,visited):
        visited[v]=True
        for u in G[v]:
            if not visited[u]:
                DFS(G,u,visited)
    
    DFS(G,0,visited)
    for i in range(n):
        if not visited[i]:
            Counter+=1
            DFS(G,i,visited)
    
    return Counter

GL = [[4,5,1],
      [5,6,2,0],
      [6,7,1],
      [7,6],
      [0],
      [0,1],
      [1,2,3],
      [2,3]]

print(CCC(GL))
