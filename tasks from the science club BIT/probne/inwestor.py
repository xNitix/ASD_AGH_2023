def inwestor ( T ):
    def minimum(T):
        n = len(T)
        inf = float("inf")
        dp = [[inf for _ in range(n)]for _ in range(n)]
        dp[0][0] = T[0]
        for i in range(n):
            for j in range(i,n):
                dp[i][j] = min(T[j],dp[i][j-1])
        return dp        
    
    n = len(T)
    dp = minimum(T)
    
    maxi = -float("inf")
    for i in range(n):
        for j in range(i+1):
            maxi = max(maxi,(i-j+1)*dp[j][i])
            
    return maxi
    
        
T = [2,1,5,6,2,3]

print(inwestor(T))