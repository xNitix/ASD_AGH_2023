from queue import Queue

def rozl_sicezki(G,s,t):
    n = len(G)
    G1 = [[0 for _ in range(2*n)]for _ in range(2*n)]
    
    for i in range(n):
        for j in range(n):
            if j != i:
                if i != s :
                    G1[i+n][j] = G[i][j]
                elif i == s:
                    G1[i][j] = G[i][j]
                elif i == t :
                    continue
                elif j == s:
                    continue
        if i != s and i != t:
            G1[i][i+n] = 1 

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
    
    return fordFulkerson(G1,s,t)



G = [[0,1,0,0,0,1],
     [0,0,1,0,0,0],
     [0,0,0,1,0,1],
     [0,0,0,0,0,0],
     [0,0,0,1,0,0],
     [0,0,0,0,1,0]]

print(rozl_sicezki(G,0,3))