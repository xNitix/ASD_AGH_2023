def knapsack2D(C,W,H,WYS,WAG):
    n = len(C)
    dp = [[[0 for _ in range(WYS+1)]for _ in range(WAG+1)]for _ in range(n)]
    for i in range(W[0],WAG+1):
        for j in range(H[0],WYS+1):
            dp[0][i][j] = C[0]
    
    for i in range(1,n):
        for w in range(WAG+1):
            for h in range(WYS+1):
                if W[i] > w or H[i] > h:
                    dp[i][w][h] = dp[i-1][w][h]
                else:
                    dp[i][w][h] = max(dp[i-1][w][h],dp[i-1][w - W[i]][h - H[i]] + C[i])

    return(dp[n-1][WAG][WYS])

C = [4, 10, 2, 3, 8]
W = [10, 4, 1, 2, 6]
H = [3, 9, 12, 4, 2]

MaxW = 12
MaxH = 20

print(knapsack2D(C, W, H, MaxH, MaxW))