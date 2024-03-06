def prom(T,L):
    n = len(T)
    dp = [[False for _ in range(L+1)]for _  in range(n)]
    dp[0][0] = True
    dp[0][T[0]] = True
    suma = [0 for _ in range(n)]
    suma[0] = T[0]
    for i in range(1,n):
        suma[i] = suma[i-1]+T[i]
    
    for i in range(n-1):
        zmiana = 0
        for j in range(L+1):
            if dp[i][j]:
                if j + T[i+1] <= L:
                    dp[i+1][j + T[i+1]] = True
                    # dp[i+1][j + T[i+1]][1] += dp[i][j][1]
                    # dp[i+1][j + T[i+1]][1].append(i)
                    zmiana+=1
                    
                if suma[i+1] - j <= L:
                    dp[i+1][j] = True
                    # dp[i+1][suma[i+1] - j][1] += dp[i][j][1]
                    # dp[i+1][suma[i+1] - j][1].append(i)
                    zmiana+=1
        if zmiana == 0:
            break

    print(*dp,sep='\n')
    

T = [2,1,4,2,3]
L = 7

print(prom(T,L))