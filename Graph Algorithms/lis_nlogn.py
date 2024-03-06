def binary_search(T,start,end,val):
        while (start < end):
            pivot = (start+end) // 2
            
            if T[pivot] == val:
                return pivot 
            
            if T[pivot] < val:
                start = pivot + 1 
            else:
                end = pivot 
    
        return start
            
            
def lis_nlogn(T):
    n = len(T)
    inf = float("inf")
    res = [-inf]
    for i in range(n):
        if T[i] > res[len(res)-1]:
            res.append(T[i])
        elif T[i] == res[len(res)-1]:
            continue
        else:
            indx = binary_search(res,0,len(res)-1,T[i])
            res[indx] = T[i]
            
    return len(res)-1