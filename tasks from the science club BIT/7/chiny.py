def chiny(T,k):
    n = len(T)
    
    miasta = 0
    
    i = 0
    last = 0
    ost_m = 0
    while i < n:
        if abs(i - last) < k:
            if T[i] == 1:
                ost_m = i
            i+=1
            continue
        
        if abs(i - last - k + 1) < k and ost_m != 0:
            last = ost_m
            ost_m = 0
            miasta+=1
            i+=1
        elif ost_m == 0 and abs(i - last - k + 1) < k:
            i+=1
        elif T[i] == 1 and abs(i - last - k + 1) <= k:
            last = i
            miasta+=1
            i+=1
            
        else:
            return -1
        
    return miasta

T=[0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1]
k=3  

print(chiny(T,k))
        