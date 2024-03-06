def matrix(A):
    n = len(A)
    inf = float("inf")
    dp = [[inf for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
        
    for i in range(n - 1):
        dp[i][i + 1] = A[i][0] * A[i][1] * A[i + 1][1]
        
    for i in range(n):
        for j in range(i):
            for k in range(j,i+1):
                dp[j][i] = min(dp[j][i],dp[j][k] + dp[k][i] + A[j][0] * A[k][1] * A[i][1])
    
    print(dp)
    