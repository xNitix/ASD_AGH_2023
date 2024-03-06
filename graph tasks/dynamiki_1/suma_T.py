def subsetSum(A,sum_):
    n = len(A)
    dp = [[False] *(sum_+1) for _ in range(n+1)] 

    for i in range(n+1):
        dp[i][0] = True

    for i in range(n+1):
        for j in range(1,sum_+1):

            if j < A[i-1]:
                dp[i][j] = dp[i-1][j]

            else:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-A[i-1]])

    return dp

A= [0,7,1,2,6]
t = 3

print(subsetSum(A,t))

[[True, False, False, False],
 [True, False, False, False],
 [True, False, False, False],
 [True, True, False, False],
 [True, True, True, True],
 [True, True, True, True]]
