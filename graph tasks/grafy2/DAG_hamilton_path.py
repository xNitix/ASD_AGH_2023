# Sciezka Hamiltona w Dagu - Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz. 
# W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi
# czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym (DAG).
# Sortujemy topologiczne wierzcholki grafu (puszczamy dfs i po przetworzeniu calego danego wierzcholka dopisujemy go NA POCZATKU(reversed) listy)
# Nastepnie sprawdzamy czy w liscie miedzy kazda para sasiedznych wierzcholkow jest bezposrednia krawedz, jesli tak jest to graf posiada
# sciezke hamiltona 
# zlozonosc : O(V+E) - zlosnosc sortowania topologicznego (DFS)

def is_hamilton_path(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    edges_sorted = []
    
    def DFS(G,u,visited,parents,edges):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS(G,v,visited,parents,edges)
        edges.append(u)
    
    for i in range(n):
        if not visited[i]:
            DFS(G,i,visited,parent,edges_sorted)
    
    edges_sorted.reverse()
    
    for i in range(n-1):
        flag = 0
        for v in G[edges_sorted[i]]:
            if v == edges_sorted[i+1]:
                flag = 1
                break
        if flag == 0:
            return False
    
    return True,edges_sorted

G = [[1,2],
     [2,3],
     [4,5],
     [2,5],
     [5],
     []]
                
print(is_hamilton_path(G))

