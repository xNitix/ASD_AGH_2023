#Zlozonosc : O(V^(1/2)*E)

def Hopcroft_karp(T):
    n = len(T)
    przypisania = [None for _ in range(n+1)]
    czy_zat = [False for _ in range(n)]
    skojarzenia = 0
    
    def przypis(v,przypisania):
        nonlocal skojarzenia
        for u in T[v]:
            if przypisania[u] == None:
                przypisania[u] = v
                czy_zat[v] = True
                skojarzenia+=1
                return 
    
    for i in range(n):
        przypis(i,przypisania)
    
    if skojarzenia == n:
        return skojarzenia
        
    def DFS(u,visited,przypisania):
        for v in T[u]:
            if not visited[v]:
                visited[v] = True
                if przypisania[v] == None:
                    przypisania[v] = u
                    return True
                elif DFS(przypisania[v],visited,przypisania):
                    przypisania[v] = u
                    return True
        return False
                
    
    for i in range(n):
        if not czy_zat[i]:
            visited = [False for _ in range(n)]
            if DFS(i,visited,przypisania):
                skojarzenia += 1
    
    return skojarzenia