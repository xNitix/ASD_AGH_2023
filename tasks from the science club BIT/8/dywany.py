def dywany(D,C,X,Y):
    n = len(D)
    dp = [[0 for _ in range(X+1)]for _ in range(Y+1)]
    
    for i in range(n):
        x,y = D[i]
        dp[y][x] = C[i]
        dp[x][y] = C[i]
    
    for y in range(Y+1):
        for x in range(X+1):
            for i in range(n):
                x_c,y_c = D[i]
                if x_c <= x and y_c <= y:
                    dp[x][y] = max(dp[x][y],dp[x_c][y_c]+dp[x_c][y-y_c]+dp[x-x_c][y_c]+dp[x-x_c][y-y_c])
                    dp[y][x] = max(dp[y][x],dp[x_c][y_c]+dp[x_c][y-y_c]+dp[x-x_c][y_c]+dp[x-x_c][y-y_c])
    print(*dp,sep = '\n')
    return dp[Y][X]


D = [(2,3),(1,4),(2,6),(1,6),(4,6)]
C = [  2  ,  4  ,  6  ,  4  ,  3  ]
X = 6
Y = 6

print(dywany(D,C,X,Y))