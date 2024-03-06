# Algorytm Forda-Fulkersona znajdujący maksymalny przeplyw w grafie od wierzchołka s do t.

# Implementacja dla reprezentacji macierzowej.
from queue import Queue

def BFS(G, s, t, parent):
    n = len(G)
    visited = [False for _ in range(n)]

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for i in range(n):
            if G[u][i] != 0 and not visited[i]:
                parent[i] = u
                visited[i] = True
                q.put(i)

    return visited[t]


def fordFulkerson(G, s, t):
    n = len(G)
    parent = [False for _ in range(n)]
    maxFlow = 0

    while BFS(G, s, t, parent):
        u = t
        mini = float("inf")

        while u != s:
            mini = min(mini, G[parent[u]][u])
            u = parent[u]

        maxFlow += mini

        u = t
        while u != s:
            G[parent[u]][u] -= mini
            G[u][parent[u]] += mini
            u = parent[u]

    return maxFlow