class Node:
    def __init__(self, idx):
        self.indx = idx
        self.parent = self


def findSet(x):
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent


def union(x, y):
    x = findSet(x)
    y = findSet(y)

    if x.indx < y.indx:
        y.parent = x

    elif y.indx < x.indx:
        x.parent = y

    else:
        x.parent = y


def Kruskal(edges,n):
    edges.sort(key=lambda x: x[0])

    MST = []
    sets = [Node(i) for i in range(n)]
    
    for edge, u, v in edges:
        if findSet(sets[ord(u)-97]) != findSet(sets[ord(v)-97]):
            MST.append((edge, u, v))
            union(sets[ord(u)-97], sets[ord(v)-97])

    return sets

def graph_maker(A,B,C):
    n = len(A)
    edges = []
    for i in range(n):
        edges.append([1,A[i],B[i]])
    
    mst = Kruskal(edges,27)
    
    new = ""
    
    for i in range(len(C)):
        l = C[i]
        new += chr(findSet(mst[ord(l)-97]).indx + 97)
        
    return new


A = "abdak"
B = "fkmjd"
C = "kajd"
print(graph_maker(A,B,C))