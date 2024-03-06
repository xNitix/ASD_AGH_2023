from egz1btesty import runtests

def planets( D, C, T, E ):
    inf = float("inf")
    dp = [[inf for _ in range(E+1)]for _ in range(len(D))]
    
    dp[0][0] = 0
    
    for i in range(len(D)):
        prev = 0
        for e in range(E+1):
            if e == 0:
            # dla energi == 0
                if i != 0:
                    dp[i][e] = min(dp[i][e],dp[i-1][D[i]-D[i-1]+prev])    
                    prev += 1
            # teleporty
                if T[i][0] > i:
                    dp[T[i][0]][e] = min(dp[T[i][0]][e],dp[i][e] + T[i][1])
            # pierwsze uzupelnienie        
            elif i == 0 and e != 0:
                dp[i][e] = dp[i][e-1] + C[i]
            else:
                # funkcja
                if D[i]-D[i-1]+prev <= E:
                    dp[i][e] = min(dp[i][e],dp[i][e-1] + C[i],dp[i-1][D[i]-D[i-1]+prev])    
                    prev += 1
                else:
                    dp[i][e] = min(dp[i][e],dp[i][e-1] + C[i])
                
    return min(dp[len(D)-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

