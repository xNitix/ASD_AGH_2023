def dywany ( N ):
    inf  = float("inf")
    dp = [[inf,0] for _ in range(N+1)]
    dp[0][0]=0
    dp[1][0]=1
    
    for i in range(2,N+1):
        j = 1 
        while j**2 <= i:
            dp[i][0] = min(dp[i][0],dp[i-j**2][0] + 1)
            if dp[i][0] == dp[i-j**2][0] + 1:
                dp[i][1] = i-j**2
            j+=1
            
    i = dp[N][1]
    res = []
    if i != 0:
        res.append(i)
    else:
        return int(N**(0.5))
    
    i = dp[i][1]
    prev = 0
    while i != 0:
        res.append(i)
        prev = i
        i = dp[i][1]
    res.append(prev)
    
    return res

N = 18

print(dywany(N))