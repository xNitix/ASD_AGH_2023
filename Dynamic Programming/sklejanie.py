# 1 czy da sie uzyskac [a,b] sklejajac z innych

def pierwsze(A,a,b):
    n = len(A)
    v_max = max(max(A))
    graph = [[]for _ in range(v_max+1)]
    
    for i in range(n):
        x,y = A[i]
        graph[x].append(y)
    
    visited = [False for _ in range(v_max+1)]
    def DFS_visit(v):
           visited[v] = True
           for u in graph[v]:
            if not visited[u]:
                DFS_visit(u)
                
    DFS_visit(a)
    return visited[b]

# 2 najdluzszy sklejajac max k

def drugie(A,k):
    n = len(A)
    dp = [[0,0] for _ in range(n)]
    A.sort(key = lambda x : x[0])
    A.sort(key = lambda x : x[1])
    for i in range(n):
        dp[i]=[A[i],1]
    
    for i in range(1,n):
        for j in range(i):
            if A[i][0] == dp[j][0][1] and dp[j][1] < k:
                dp[i][0] = [dp[j][0][0],A[i][1]]
                dp[i][1] = dp[j][1] + 1
                
    return dp[n-1][0]

# 3 najtaniej - dijkstra

A = [[4, 5], [2, 4], [1, 3], [3, 6], [5, 7]]
print(pierwsze(A,1,6))
print(drugie(A,3))