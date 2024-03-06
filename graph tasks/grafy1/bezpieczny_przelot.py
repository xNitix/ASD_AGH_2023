# bezpieczny przelot - Dany jest graf G = (V, E), którego wierzcholki reprezentuja punkty
# nawigacyjne nad Bajtocja, a krawedzie reprezentuja korytarze powietrzne miedzy tymi punktami. Kazdy
# korytarz powietrzny powiazany jest z optymalnym pulapem przelotu (wyrazonym w metrach)
# Przepisy dopuszczaja przelot danym korytarzem jesli pula samolotu rózmi sie od optymalnego najwyzej o t
# metrów. Prosze zaproponowaé algortm, kóry sprawdza czy istnieje mozliwosc przelotu
# z zadanego punktu do zadanego punktu w taki sposób, zeby samolot nigdy nie zmienial pulapu.
# Znajdujemy najmniejsza wartosc i szukamy w widelkach jej +/- t, jesli nie bedzie to wieskzamy nasze "ono" o 2 t
# wtedy prz3ejdziemy przesz wszytskie mozliwe przedzialy
# Zlozonosc : O(p(V+E)) gdzie p to ilosc roznych mozliwych widelek pulap +/- t, a (V+E) to zloznosc DFS na reprezentacji listowej

def fly(G,s,k,t):
    n = len(G)
    inf = float("inf")
    mini = inf
    maxi = -inf
    
    for i in range(n):
        for v,wagi in G[i]:
            if wagi < mini:
                mini = wagi
            elif wagi > maxi:
                maxi = wagi
                
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    
    def DFSVisit(G,s,k,t,pulap,visited,parents):
        visited[s] = True
        for v, wagi in G[s]:
            if not visited[v] and (pulap >= wagi-t and pulap <= wagi + t):
                parent[v] = s
                DFSVisit(G,v,k,t,pulap,visited,parents)
        return visited[k]
    
    if DFSVisit(G,s,k,t,mini,visited,parent):
        return True
    
    pivot = mini
    while mini < maxi:    
        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]        
        pivot = pivot + 2*t
        mini = pivot
        if DFSVisit(G,s,k,t,pivot,visited,parent):
            return True
        
    return False
        
def undirected_weighted_graph_list(E):
    # Find the number of vertices
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    # Create a graph matrix
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    return G        

E = [(0, 1, 100), (1, 2, 110), (2, 3, 135), (2, 4, 120), (0, 4, 120), (4, 5, 90), (2, 5, 95), (5, 3, 90),
     (0, 7, 115), (7, 6, 120), (4, 6, 95), (5, 6, 110), (6, 3, 105)]
G = undirected_weighted_graph_list(E)

print(fly(G,0,3,15))