from math import inf
def bridge(G):
    n = len(G)
    visited=[False for _ in range(n)]
    parent_t=[None for _ in range(n)]
    time_vis=[0 for _ in range(n)]
    low = [inf for _ in range(n)]
    time = 0

    def DFS(G,u,visited,parent_t,time_vis,low,time):
        visited[u] = True
        time_vis[u]=time
        time+=1
        low[u]=time_vis[u]
        for v in G[u]:
            if visited[v] == False:
                parent_t[v]=u
                DFS(G,v,visited,parent_t,time_vis,low,time)
                low[u]=min(low[u],low[v])
            elif parent_t[u] != v:
                low[u]=min(low[u],time_vis[v])

    bridges = []
    for i in range(n):
        if visited[i] == False:
            DFS(G,i,visited,parent_t,time_vis,low,time)
    for i in range(n):
        if time_vis[i] == low[i] and parent_t[i] != None:
            bridges.append([parent_t[i],i])
    return bridges

def DFS_Euler_path(G):
    # sprawdzam czy istnieje cykl eulera
    for i in range(len(G)):
        edges = 0
        for j in range(len(G[i])):
            if G[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return False
    
    def DFS_Euler(G,vertex,res):
        for i in range(len(G)):
            if G[vertex][i] == 1:
                G[vertex][i] = 0
                G[i][vertex] = 0
                DFS_Euler(G, i, res)
        res.append(vertex)
    
    res = [] 
    DFS_Euler(G,0,res)
    reversed(res)
    return res

def hamilton(G):
    n = len(G)
    flaga=0
    res=[]
    lista=[ i for i in range(n)]
    
    def permutacje(lista,indx):
        if indx < len(lista):
            for i in range(indx,len(lista)):
                lista[i],lista[indx]=lista[indx],lista[i]
                permutacje(lista,indx+1)
                lista[i],lista[indx]=lista[indx],lista[i]
        else:
            print(lista)
        
        
    def permutacje(G,lista,indx):
        if indx < len(lista):
            for i in range(indx,len(lista)):
                lista[i],lista[indx]=lista[indx],lista[i]
                permutacje(G,lista,indx+1)
                lista[i],lista[indx]=lista[indx],lista[i]
        else:
            nonlocal res
            flaga = 0
            for i in range(len(lista)-1):
                if G[i][i+1] == G[i+1][i] == 0:
                    flaga = 1
                    break
            if flaga == 0:
                res=lista
        return False
    permutacje(G, lista, 0)
    return res

def DFS_sort_topologiczne(G):
    n = len(G)
    time = 0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    res = []
    
    def DFSVisit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        nonlocal res
        
        time +=1
        visited[u]=time
        
        for v in G[u]:
            if visited[v] == False:
                parent[v]=u
                DFSVisit(G,v)
                
        res.append(u)
        time +=1
    
    for i in range(len(G)):
        if visited[i] == False:
            DFSVisit(G,i)
    patch=[] 
    for i in range(len(res)-1,-1,-1):
        patch.append(res[i])
    return patch
        
def Bellman_Ford(G,s):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n)]
    parents = [None for _ in range(n)]
    wagi[s] = 0
    
    def relax(u,v,wagi,edge):
        if wagi[v] > wagi[u] + edge:
            wagi[v] = wagi[u] + edge
            return True
        return False
    
    for _ in range(n-1):
        for u in range(n):
            for v,edge in G[u]:
                if relax(u,v,wagi,edge):
                    parents[v] = u
    # sprawdzanie czy ujemny cykl
    for u in range(n):
        for v,edge in G[u]:
            if relax(u,v,wagi,edge):
                return None
    
    return wagi,s

graph=[[(1,3),(3,3),(4,2)],
       [(2,-7)],
       [(3,8)],
       [(4,-2),(1,-1)],
       [],
]

from queue import PriorityQueue
def prim(G):
    inf = float("inf")
    n = len(G)
    visited = [False for _ in range(n)]
    wagi = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    Que = PriorityQueue()
    wagi[0] = 0
    Que.put([wagi[0],0])
    
    while not Que.empty():
        _, u = Que.get()
        visited[u] = True
        for v,edge in G[u]:
            if not visited[v]:
                 if wagi[v] > edge:
                     wagi[v] = edge
                     parent[v] = u
                     Que.put([wagi[v],v])
    
    MST=[]
    for i in range(n):
        if parent[i] != None:
             MST.append([parent[i],i,wagi[i]])
    
    return MST


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


def Kruskal(G):
    n = len(G)
    edges = []

    for u in range(len(G)):
        for v,edge in G[u]:
            edges.append((edge, u, v))

    edges.sort(key=lambda x: x[0])

    MST = []
    sets = [Node(i) for i in range(n)]

    # przechodzi po krawędziach i jeśli wierzchołki są w osobnych zbiorach (czyli nie ma połączenia między u a v) to dodaję krawędź do MST
    for edge, u, v in edges:
        if findSet(sets[u]) != findSet(sets[v]):
            MST.append((u, v ,edge))
            union(sets[u], sets[v])

    return MST


G =[
    [[1,8],[2,7]],
    [[0,8],[2,10]],
    [[0,7],[1,10],[6,3]],
    [[5,1],[4,1]],
    [[5,4],[3,1]],
    [[3,1],[4,4],[6,14]],
    [[2,3],[7,7],[5,14]],
    [[6,7]]
    ]

print(Kruskal(G))