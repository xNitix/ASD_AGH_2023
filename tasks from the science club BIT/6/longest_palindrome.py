# 2*n^2
def longest(s):
    n = len(s)
    dp = [[0 for _ in range(n)]for _ in range(n)]
    
    # F[i][i] = 1
    for i in range(n):
        dp[i][i] = 1
    
    # if s[i]==s[i+1] -> F[i][i+1] = 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
    
    # if s[i] == s[j] and f[j+1][i-1] > 0
    for i in range(2,n):
        for j in range(i):
            if s[i] == s[j]:
                if dp[j+1][i-1] > 0:
                    dp[j][i] = dp[j+1][i-1] + 2
    
    # find sol
    max_len = 0
    st = 0
    end = 0
    
    for i in range(n):
        for j in range(i):
            if dp[j][i] > max_len:
                max_len = dp[j][i]
                st = j
                end = i
    
    print(*dp,sep='\n')

    return max_len,s[st:end+1]
    
    
string = "aacdidck"

print("wynik : ", longest(string))