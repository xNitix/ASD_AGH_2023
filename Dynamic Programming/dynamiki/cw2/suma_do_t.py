def suma(A,T):
    n = len(A)
    dp = [[False for _ in range(T+1)]for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = True
    
    dp[0][A[0]] = True
    
    for i in range(1,n):
        for j in range(1,T+1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j - A[i] >= 0:
                dp[i][j] = dp[i-1][j - A[i]] 
                
    print(*dp,sep = '\n')
    return dp[n-1][T]    
    
A = [2,1,4,2,2]
T = 4
print(suma(A,T))
                
            