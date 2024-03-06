def ksuma( T, k):
    n = len(T)
    inf = float("inf")
    ile = [inf for _ in range(n)]
    
    for i in range(k):
        ile[i] = T[i]
        
    for i in range(k,n):
        ile[i] = min(ile[i-k:i])+ T[i]
    
    mini = inf 
    
    for j in range(n-k,n):
        mini = min(mini,ile[j])
        
    return mini

T = [1,2,3,4,6,15,8,7]
k = 4

print(ksuma(T,k))