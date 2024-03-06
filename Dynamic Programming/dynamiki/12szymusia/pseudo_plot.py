def autostrady(T,k):
    n = len(T)
    inf = float("inf")
    sumy = [0 for _ in range(n)]
    sumy[0] = T[0]
    dp = [[inf for _ in range(n)]for _ in range(k)]
    
    for i in range(1,n):
        sumy[i] = sumy[i-1] + T[i]
        dp[0][i] = sumy[i]
    dp[0][0] = T[0]
    
    for i in range(1,k):
        for j in range(i,n):
            for m in range(i-1,j):
                dp[i][j] = min(dp[i][j],max(sumy[j] - sumy[m], dp[i-1][m]))
    return dp[k-1][n-1]

T = [5,10,30,20,15]
k = 3

print(autostrady(T,k))
    
    
        