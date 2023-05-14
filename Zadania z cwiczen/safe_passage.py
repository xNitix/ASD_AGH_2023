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
