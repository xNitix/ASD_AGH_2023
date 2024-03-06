def amazon(A):
    n = len(A)
    steps = [0 for _  in range(n)]
    steps[0] = 1
    
    for i in range(n):
        dl = A[i]
        for j in range(1,dl+1):
            steps[i+j] += steps[i]
            
    return steps

A = [1,3,2,1,0]

print(amazon(A))