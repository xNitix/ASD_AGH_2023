def podciag(A,B):
    n = len(A)
    dp = [[0 for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        if A[0] == B[i]:
            dp[0][i] = 1
        else:
            dp[0][i] = dp[0][i-1]
    
    for i in range(n):
        if A[i] == B[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]
    maxi = 1    
    for i in range(1,n):
        for j in range(1,n):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                maxi = max(maxi,dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                maxi = max(maxi,dp[i][j])
    print(*dp,sep = '\n')
    return maxi
    
    
A = [6,0,1,2,2]
B = [7,8,0,1,7]

print(podciag(A,B))