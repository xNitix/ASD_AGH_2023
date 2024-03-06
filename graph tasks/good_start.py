# Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?
# Sortujemy krawedzie topologiczne, a nastepnie wykonujemy relaxacje wszystkich wierzcholkow
# w kojenosci sortowani topologicnzego
# Zloznonosc : O(V+E) sortowanie topologiczne(DFS) + stala w postaci relaxacji
def shortest_path_dag(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    
    def Sort_top(G,visited):
        res = []
        def DFSVisit(G,u,visited,res):
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    DFSVisit(G,v,visited,res)
            res.append(u)
        
        for i in range(len(G)):
            if not visited[i]:
                DFSVisit(G,i,visited,res)
        
        res.reverse()
        return res 
    
    sort_t=Sort_top(G,visited)

    inf = float("int")
    parent = [None for _ in range(n)]
    dist = [inf for _ in range(n)]
    dist[s]
    
    
    
    




G = [[1,2],
     [2,3],
     [4,5],
     [2,5],
     [5],
     []]


print(shortest_path_dag(G,s))