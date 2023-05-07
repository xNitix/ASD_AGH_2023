# Zany operator telefonii komórkowej Pause postanowil zakonczy dzialalnose w
# Polsce. Jednym z glównych elementow calej procedury jest wylaczenie wszystkich stacji nadawczych (kore
# tworza spójny graf polaczen). Ze wzgledów technologicznych urzadzenia nalezy wylaczac pojedynczo a ope-
# ratorowi dodatkowo zalezy na tym, by podezas calego procesu wszyscy abonenci znajdujacy sie w zasiegu
# dzialajacych stacji mogli sie ze soba laczyc (czyli by graf pozostal spójny). Prosze zaproponowac algorytm
# podajacy kolejnosc wylaczania stacji.
# Wykonujemy DFS z zapisywaniem czasow przetworzenia, nastpenie odlaczamy wiercholki (stacje) w kolejnosci malejacych czasow prztworzenia
# Zlozonosc : O(V+E) taka sama jak DFS dla listy

def Pasue(G):
    n = len(G)
    visited = [False for _ in range(n)]
    time = 0 
    visited[0]=time
    off=[-1 for _ in range(n)]
    
    def DFS(G,u,visited):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS(G,v,visited)
        off[time]=u
        time += 1
        
    
    for i in range(n):
        if not visited[i]:
            DFS(G,i,visited)
    
    return off
