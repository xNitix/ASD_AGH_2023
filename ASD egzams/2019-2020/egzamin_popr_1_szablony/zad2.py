from zad2testy import runtests
from math import sqrt
from math import ceil

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
    slownik = {}

    for i in range(n):
        slownik[G[i]] = i
        for j in range(i,n):
            edge = sqrt((G[i][0] - G[j][0])**2 + (G[i][1] - G[j][1])**2)
            edges.append([edge,G[i],G[j]]) 

    edges.sort(key=lambda x: x[0])
    
    l_indx = 0
    p_indx = n-1
    
    inf = float("inf")
    mini = inf
    
    while p_indx < len(edges):
        edges2 = edges[l_indx:p_indx+1]
        MST = []
        sets = [Node(i) for i in range(n)]
        
        for edge, u, v in edges2:
            if findSet(sets[slownik[u]]) != findSet(sets[slownik[v]]):
                MST.append((edge, u, v))
                union(sets[slownik[u]], sets[slownik[v]])
                
        if len(MST) == n-1:
            #print(MST)
            #print(len(MST))
            day = ceil(MST[len(MST)-1][0])-ceil(MST[0][0])
            #print(day)
            mini = min(mini,day)
            
        l_indx+=1
        p_indx+=1

    return mini

def highway(A):
    return Kruskal(A)
        

runtests( highway ) 
