def maxim(T,k):
    inf = float("inf")
    n = len(T)
    dp = [[- inf for _ in range(k)]for _ in range(n)]
    suma = [0 for _ in range(n)]
    suma[0] = T[0]
    for i in range(1,n):
        suma[i] = suma[i-1] + T[i]
    
    for i in range(n):
        dp[i][0] = suma[i]
    
    for c in range(1,k):
        for i in range(n):
            for j in range(i-1,-1,-1):
                dp[i][c] = max(dp[i][c],min(suma[i] - suma[j],dp[j][c-1]))
    
    print(*dp,sep='\n')
    return dp[n-1][k-1]
    
T = [3,7,6,1,2,4]
K = 3

print("wynik : ",maxim(T,K))
        