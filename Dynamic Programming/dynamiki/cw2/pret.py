def precior(T):
    n = len(T)
    koszty = T[:]
    
    for i in range(1,n):
        for cut in range(i):
            koszty[i] = max(koszty[i],koszty[i-cut] + T[cut])
    
    return koszty[n-1]

T = [(3,3),(1,1),(5,8),(7,12)]

print(precior(T))