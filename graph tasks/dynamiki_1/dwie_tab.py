def lcs(A, B):
    a = len(A)
    b = len(B)
    
    # slowo A- wiersze, słowo B - kolumny
    dp = [[0] * (b) for _ in range(a)]

    for a1 in range(a):
        if A[a1] == B[0]:
            dp[a1][0] = 1

    for b1 in range(b):
        if A[0] == B[b1]:
            dp[0][b1] = 1

    for a1 in range(1, a):
        for b1 in range(1, b):
            if A[a1] == B[b1]:
                dp[a1][b1] = dp[a1 - 1][b1 - 1] + 1
            else:
                dp[a1][b1] = max(dp[a1 - 1][b1], dp[a1][b1 - 1])

    res = []
    a1, b1 = a - 1, b - 1

    while a1 >= 0 and b1 >= 0:
        if A[a1] == B[b1]:
            res.append(A[a1])
            a1 -= 1
            b1 -= 1
        elif dp[a1 - 1][b1] > dp[a1][b1 - 1]:
            a1 -= 1
        else:
            b1 -= 1
    
    return res[::-1]

A = [3,5,1,0,2,10]
B = [7,8,0,2,1,6]
