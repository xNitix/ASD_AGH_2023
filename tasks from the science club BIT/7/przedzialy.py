def longest(T,k):
    n = len(T)
    T.sort(key = lambda x : x[1])
    inf = float("inf")
    
    min_abs = inf
    min_p = 0
    min_k = 0
    
    def in_(x,y,x1,y1):
        if y <= x1 :
            return True
        if y1 <= x :
            return True
        return False 
    
    
    for i in range(n):
        curr_p = T[i][0]
        curr_k = T[i][1]
        curr_ka = 1
        for j in range(i+1,n):
            if in_(curr_p,curr_k,T[j][0],T[j][1]):
                curr_ka+=1
                curr_p = min(curr_p,T[j][0])
                curr_k = max(curr_k,T[j][1])
            if curr_ka == k:
                if abs(curr_k-curr_p) < min_abs:
                    min_p = curr_p
                    min_k = curr_k
                    min_abs = abs(curr_k-curr_p)
                break
    
    if min_p == min_k == 0:
        return "brok"
    
    return [min_p,min_k],min_abs


T = [[7,10],[8,9],[1,2],[2,7],[6,12],[3,9],[6,7],[5,6]]

print(longest(T,3))