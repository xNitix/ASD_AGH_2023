from math import ceil, sqrt
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

def dist(xi, yi, xj, yj):
    return ceil(sqrt((xi - xj) ** 2 + (yi - yj) ** 2))


def Autodrady(G):
    inf = float("inf")
    edges = []
    n = len(G)

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, dist(G[i][0], G[i][1], G[j][0], G[j][1])))
            
    edges.sort(key=lambda x: x[2])
    m = len(edges)
    res = inf

    for i in range(m-n+1):
        sets = [Node(i) for i in range(n)]
        cur_min = inf
        cur_max = -inf
        
        cnt = 0
        for j in range(i,m):
            u,v,edge = edges[j]
            if findSet(sets[u]) != findSet(sets[v]):
                union(sets[u],sets[v])
                cnt += 1
                cur_max=max(cur_max,edge)
                cur_min=min(cur_min,edge)
        
        if cnt == n-1:
            res = min(res,abs(cur_max-cur_min))
            
    return res
            

P = [(5, 5), (3, -5), (0, 3), (-5, 0)]

print(Autodrady(P))