def akademik ( T ):
    n = len(T)
    maszyny = [None for _ in range(n+1)]
    czy_zat = [False for _ in range(n)]
    skojarzenia = 0
    ile_non=0
    G = [[]for _ in range(n)]
    for i in range(n):
        flag = 1
        for j in range(3):
            if T[i][j] != None:
                G[i].append(T[i][j])
                flag = 0
        if flag:
            ile_non+=1
    

    
    def przypis(v,maszyny):
        nonlocal skojarzenia
        for u in G[v]:
            if maszyny[u] == None:
                maszyny[u] = v
                czy_zat[v] = True
                skojarzenia+=1
                return 
    
    for i in range(n):
        przypis(i,maszyny)
    
    if skojarzenia == n:
        return skojarzenia
        
    def DFS(u,visited,maszyny):
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                if maszyny[v] == None:
                    maszyny[v] = u
                    return True
                elif DFS(maszyny[v],visited,maszyny):
                    maszyny[v] = u
                    return True
        return False
                
    
    for i in range(n):
        if not czy_zat[i]:
            visited = [False for _ in range(n)]
            if DFS(i,visited,maszyny):
                skojarzenia += 1
    
    return n - skojarzenia - ile_non


T = [(2, 3, None) ,(0, 1, 3),(0, 2, None) ,(1,3,4), (2,3,None) ]
print(akademik(T))