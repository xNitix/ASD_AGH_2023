def plecak(W,C,pojemnosc):
    n = len(W)
    dp = [[0 for _ in range(pojemnosc+1)]for _ in range(n)]
    
    #pierwszy przedmiot 
    for i in range(W[0],pojemnosc + 1):
        dp[0][i] = C[0]
        
    for i in range(1,n):
        for j in range(1,pojemnosc+1):
            
            if W[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                print(dp[i-1][j-W[i]],i,j-W[i],j)
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-W[i]] + C[i])
                
    #return dp[n-1][pojemnosc]
    
    def przedmioty(i, pojemnosc):
            if i < 0:
                return []

            elif i == 0:
                if W[0] <= pojemnosc:
                    return [0]
                else:
                    return []
            else:
                if dp[i][pojemnosc] == dp[i - 1][pojemnosc]:
                    return przedmioty(i - 1, pojemnosc)
                else:
                    return przedmioty(i - 1, pojemnosc - W[i]) + [i]
    print(*dp,sep='\n')
    return przedmioty(n-1,pojemnosc)
        

W = [2,2,2,3]
C = [10,5,7,14]
pojemnosc = 5
                
print(plecak(W,C,pojemnosc))