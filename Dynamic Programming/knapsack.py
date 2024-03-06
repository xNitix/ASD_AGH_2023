def knapsack(W,C,P):
    n = len(W)
    dp = [[0 for _ in range(P+1)]for _ in range(n)]

    for i in range(W[0],P+1):
        dp[0][i] = C[0]
    
    for i in range(1,n):
        for j in range(P+1):
            if W[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j - W[i]] + C[i])
    
    print(*dp,sep='\n')


W = [2,2,2,3]
C = [10,5,7,14]
pojemnosc = 5

print(knapsack(W,C,pojemnosc))