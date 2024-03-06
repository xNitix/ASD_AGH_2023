from collections import deque

def BFS(G,s):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    d=[-1 for _ in range(n)]
    Queue=deque()
    Queue.append(s)
    visited[s]=True
    d[s]=0
    while len(Queue) != 0:
        u = Queue.popleft()
        print(u)
        for v in G[u]:
            if visited[v] == False:
                d[v]=d[u]+1
                parent[v]=u
                visited[v]=True
                Queue.append(v)