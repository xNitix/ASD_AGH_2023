def talerze(T,P):
    n = len(T)
    inf = float("inf")
    dp = [[-inf for _ in range(P+1)]for _ in range(n)]
    sumy = [[0]for _ in range(n)]
    
    for i in range(n):
        for j in range(len(T[i])):
            if j == 0:
                sumy[i].append(T[i][j])
            else:
                sumy[i].append(T[i][j]+sumy[i][len(sumy[i])-1])
    
    for i in range(n):
        for j in range(len(T[i]),P+1):
            sumy[i].append(-inf)
    
    # pierwsze uzupelnienie
    for i in range(1,P+1):
        if i < len(sumy[0]):
            dp[0][i] = sumy[0][i]
        else:
            dp[0][i] = dp[0][i-1]
    
    for i in range(1,n):
        for j in range(P+1):
            for k in range(0,j+1):
                # funkcja
                if j > 1:
                    dp[i][j] = max(dp[i][j],dp[i-1][k] + sumy[i][j-k])
                elif j == 1:
                    dp[i][j] = max(sumy[i][1],dp[i-1][1])
    
    return dp[n-1][P]
                    
    # print(sumy)
    # print(*dp,sep = '\n')
    
    
Stosy = [[1,0,2],
         [2,-1,1],
         [1,0,3]
         ]

P = 4

print(talerze(Stosy,P))