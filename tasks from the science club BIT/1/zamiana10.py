def count_sort(T,k):
    n = len(T)
    C = [0 for _ in range(k+1)]
    res = [0 for _ in range(n)]
    for i in range(n):
        C[T[i]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        res[C[T[i]]-1] = T[i]
        C[T[i]] -= 1
    return res

def bombel(T):
    n = len(T)
    for i in range(n):
        for j in range(n-1):
            if T[j] > T[j+1]:
                T[j+1],T[j] = T[j],T[j+1]

def sort(T,k):
    n = len(T)
    out_range = []
    good = []
    for i in range(n):
        if 0 <= T[i] <= k:
            good.append(T[i])
        else:
            out_range.append(T[i])
    new_good = count_sort(good,k)
    bombel(out_range)
    indx_good = 0
    indx_out = 0
    for i in range(n):
        if indx_out < len(out_range) and out_range[indx_out] <= 0:
            T[i] = out_range[indx_out]
            indx_out+=1
        elif indx_good < len(new_good) and new_good[indx_good] <= k:
            T[i] = new_good[indx_good]
            indx_good += 1
        else:
            T[i] = out_range[indx_out]
            indx_out += 1
    return T
            
T = [-20,-8,1,0,-1,-60,4,7,100,-2,10,9,20,30,-7,1000]

print(sort(T,10))
    
    