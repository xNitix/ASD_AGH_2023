from queue import Queue
def sklepy(S,F,G):
    def BFS(s,t,parents,G):
        visited = [False for _ in range(len(G))]
        Que = Queue()
        visited[s] = True
        Que.put(s)
        while not Que.empty() :
            u = Que.get()

            for v in range(len(G[u])):
                if not visited[v] and v!=u and G[u][v] != 0:
                   visited[v] = True
                   parents[v] = u
                   Que.put(v)
        return visited[t]
    
    def ford_fulker(G,s,t):
        parents = [None for _ in range(len(G))]
        max_flow = 0
        
        while BFS(s,t,parents,G):
            inf = float("inf")
            minimalna = inf
            
            par = t
            while parents[par] != None:
                minimalna = min(minimalna,G[parents[par]][par])
                par = parents[par]
                
            max_flow += minimalna
            # aktualizacja kraw
            
            par = t
            while parents[par] != None:
                G[par][parents[par]] += minimalna
                G[parents[par]][par] -= minimalna
                par = parents[par]
                
        return max_flow
            
    # nowy graf
    n = len(G)
    for i in range(len(S)):
        for j in range(n):
            if G[i][j] != 0:
                G[j][i] = G[i][j]
                G[i][j] = 0
    G.append([0 for _ in range(n)])
    G.append([0 for _ in range(n)])
    
    for i in range(len(G)):
        G[i].append(0)
        G[i].append(0)
    
    for i in range(len(S)):
        G[i][len(G)-2] = S[i]
        
    for i in range(len(F)):
        G[len(G)-1][len(S)+i] = F[i]
    
    max_F = ford_fulker(G,len(G)-1,len(G)-2)
    
    suma = 0
    
    for i in range(len(S)):
        suma += S[i]
    
    return suma == max_F        


Sklepy = [5,4,8,3]
Fabryki = [9,7,6]
G = [[0,0,0,0,5,0,0],
     [0,0,0,0,6,0,4],
     [0,0,0,0,7,4,0],
     [0,0,0,0,0,5,7],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0]
     ]


print(sklepy(Sklepy,Fabryki,G))


