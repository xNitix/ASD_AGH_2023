class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = self
        self.rank = 0


def findSet(x):
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent


def union(x, y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        y.parent = x

    elif y.rank > x.rank:
        x.parent = y

    else:
        x.parent = y
        y.rank += 1


def Kruskal(edges,n):
    edges.sort(key=lambda x: x[0])

    MST = []
    sets = [Node(i) for i in range(n)]
    
    for edge, u, v in edges:
        if findSet(sets[u]) != findSet(sets[v]):
            MST.append((edge, u, v))
            union(sets[u], sets[v])

    return MST

def lotniska(E,k):
    n = len(E)
    New_E = []
    n_count = 0
    for i in range(n):
        u,v,edge = E[i]
        n_count = max(n_count,u,v)
        if edge < k:
            New_E.append([edge,u,v])
            
    mst = Kruskal(New_E,n_count+1)
    
    graph = [[]for _ in range(n_count+1)]
    
    suma = 0
    
    for i in range(len(mst)):
        edge,u,v = mst[i]
        graph[u].append(v)
        graph[v].append(u)
        suma += edge
    
    visited = [False for _ in range(n_count+1)]
      
    def dfs_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
                
    lotniska_count = 0
    for i in range(n_count+1):
        if not visited[i]:
            dfs_visit(graph,i)
            lotniska_count+=1
    
    return suma + (lotniska_count*k)
            

E = [(0, 1, 2), (1, 2, 7), (2, 3, 2), (0, 4, 6), (1, 4, 5), (4, 2, 4), (2, 5, 3), (5, 6, 5), 
     (7, 5, 1), (8, 7, 3)]

K = 4

print(lotniska(E,K))