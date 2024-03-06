def Floyd_Warschall(G):
    n = len(G)
    inf = float("inf")
    wagi = G[:]
    parents = [[None for _ in range(n)]for _ in range(n)]
    
    def relax(i,j,k,wagi):
        if wagi[j][k] > wagi[j][i] + wagi[i][k]:
            wagi[j][k] = wagi[j][i] + wagi[i][k]
            return True
        return False
    
    
    for i in range(n):
        for j in range(n):# startowy
            for k in range(n): # koncowy
                if relax(i,j,k,wagi):
                    parents[j][k] = i
                    
    # sprawdzanie ujemnego cyklu
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if relax(i,j,k,wagi):
                    wagi[j][k] = -inf
                    parents[j][k] = -1
    
    return wagi,parents

def robot( G, P ):
    n = len(G)
    inf = float("inf")
    Graph = [[inf for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        for j in range(len(G[i])):
            Graph[i][G[i][j][0]] = G[i][j][1]
            
    Floyd_Warschall(Graph)
    
    suma = 0
    
    for i in range(len(P)-1):
        suma += Graph[P[i]][P[i+1]]
        
    return suma
    
    
G = [[(1, 3), (2, 3)],
[(0, 3), (4, 4)],
[(0, 3), (3, 1), (4, 4)],
[ (2, 1), (4, 2)],
[ (1, 4), (2, 4), (3, 2)]]
P = [0, 3, 4]
    
print(robot(G,P))