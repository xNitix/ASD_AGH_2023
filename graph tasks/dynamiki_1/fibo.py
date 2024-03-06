def fib(n):
    F = [1 for _ in range(n)]
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]

print(fib(10))