from collections import deque
def BFS_dwudzielnosc(G):
    n = len(G)
    s=0
    colors=[-1 for _ in range(n)]
    visited=[False for _ in range(n)]
    Que = deque()
    Que.append(s)
    colors[s]=1
    visited[s]=True
    while len(Que) != 0:
        u = Que.popleft()
        for v in G[u]:
            if colors[v] == -1:
                colors[v]=colors[u]%2 + 1
            if colors[v] == colors[u]:
                return False
            if visited[v] == False:
                Que.append(v)
                visited[v]=True
                   
    return True
