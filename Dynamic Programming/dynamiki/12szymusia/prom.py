def ferry(A, l):
    n = len(A)
    sum = [0 for _ in range(n)]
    sum[0] = A[0]
    for i in range(1, n):
        sum[i] = sum[i - 1] + A[i]

    dp = [[False for _ in range(l+1)]for _ in range(n)]
    
    dp[0][A[0]] = True
    dp[0][0] = True

    for i in range(n - 1):
        zmiana = 0
        for dl in range(l + 1):
            if dp[i][dl]:
                if dl + A[i + 1] <= l:
                    dp[i + 1][dl + A[i + 1]] = True
                    zmiana = 1
                    
                if sum[i + 1] - dl <= l:
                    dp[i + 1][dl] = True
                    zmiana = 1
        if not zmiana:
            print(*dp,sep='\n')
            return i+1
    print(*dp,sep='\n')
    return n


t = [2,1,4,2,3]
l = 5

print(ferry(t,l))