def plecak2d(W,H,C,p,wys):
    dp = [[0 for _ in range(p+1)]for _ in range(wys+1)]
    inf = float("inf")
    maxi = -inf
    for item in range(len(W)):
        dp[H[item]][W[item]] = max(dp[H[item]][W[item]],C[item])
        maxi = max(maxi,dp[H[item]][W[item]])
        for i in range(wys+1):
            for j in range(p+1):
                if dp[i][j] != 0:
                    if i + H[item] <= wys and j + W[item] <= p:
                        dp[i + H[item]][j + W[item]] = max(dp[i + H[item]][j + W[item]], dp[i][j] + C[item])
                        maxi = max(maxi,dp[i + H[item]][j + W[item]])
    print(*dp,sep='\n')
    return maxi
                
                
W = [5,3,7,3]
H = [4,7,1,5]
C = [10,15,5,13]
pojemnosc = 13
wysokosc = 13

print(plecak2d(W,H,C,pojemnosc,wysokosc))
