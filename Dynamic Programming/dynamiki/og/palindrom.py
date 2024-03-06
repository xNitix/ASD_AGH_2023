def palindrom(S):
    n = len(S)
    dp = [[False for _ in range(n+1)]for _ in range(n)]
    
    #dla palidromow wielkosci 1
    for i in range(n):
        dp[i][i] = True
        dp[i][n] += 1

    #dla palindromow o dl 2
    for i in range(n-1):
        if S[i] == S[i+1]:
            dp[i][i+1] = True
            dp[i][n] += 1
        else:
            dp[i][i+1] = False
            
    glob_max = 0
    glob_indx = 0
    
    for leng in range(2,n):
        for i in range(n-1):
            j = i + leng
            if j < n:
                if S[i] == S[j]:
                    if dp[i+1][j-1] and dp[i+1][i+1]:
                        dp[i][j] = True
                        dp[i][n] = max(dp[i][n],j-i+1)
                        
                if glob_max < dp[i][n]:
                    glob_max = dp[i][n]
                    glob_indx = i
                    
    return S[glob_indx:glob_indx+glob_max]


    
S = "ABCCBCZZZCBCX"

print(palindrom(S))