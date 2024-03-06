def pręt(x,T):
    n = len(T)
    ceny = [0 for _ in range(x+1)]
    ciecia = [[]for _ in range(x+1)]
    
    for i in range(n):
        if T[i][0] <= x:
            ceny[T[i][0]] = T[i][1]
            ciecia[T[i][0]].append(T[i][0])
            
    for i in range(x+1):
        for j in range(i):
            if ceny[i] < ceny[i-j]+ceny[j]:
                ceny[i] = ceny[i-j]+ceny[j]
                ciecia[i] = ciecia[i-j] + ciecia[j]
    
    return ceny[x],ciecia[x]

T = [(3,3),(1,1),(5,8),(7,12)]
x = 20

print(pręt(x,T))