def nominaly(N,T):
    n = len(N)
    inf = float("inf")
    dp = [inf for _ in range(T+1)]
    
    dp[0] = 0
    
    for ile in range(1,T+1):
        for nom in N:
            if ile - nom >= 0:
                if dp[ile] > dp[ile-nom] + 1:
                    dp[ile] = dp[ile-nom] + 1
                    
    print(dp)   
    return dp[T]

Nom = [5,7,6,4]
T = 32

print(nominaly(Nom,T))

