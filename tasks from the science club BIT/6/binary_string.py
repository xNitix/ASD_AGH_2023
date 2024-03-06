def binary(n):
    dl = [0 for _ in range(n+1)]
    dl[1] = 2
    dl[2] = 3
    
    for i in range(3,n+1):
        dl[i] = dl[i-1] + dl[i-2]
        
    return dl[n]

print(binary(10))