from zad1testy import runtests

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
    le = [1 for _ in range(n)]
    res = [-inf]
    for i in range(n):
        if T[i] > res[len(res)-1]:
            res.append(T[i])
            le[i] = len(res)
        elif T[i] == res[len(res)-1]:
            le[i] = len(res)
            continue
        else:
            indx = binary_search(res,0,len(res)-1,T[i])
            res[indx] = T[i]
            le[i] = len(res)
            
    return le

def binary_search_opp(T,start,end,val):
        while (start < end):
            pivot = (start+end) // 2
            
            if T[pivot] == val:
                return pivot 
            
            if T[pivot] > val:
                start = pivot + 1 
            else:
                end = pivot 
    
        return start

def lds(T):
    le = [1 for _ in range(len(T))]
    res = [T[0]]
    for i in range(1,len(T)):
        if T[i] < res[len(res)-1]:
            res.append(T[i])
            le[i] = len(res)
        if T[i] == res[len(res)-1]:
            le[i] = len(res)
        if T[i] > res[len(res)-1]:
            indx = binary_search_opp(res,0,len(res)-1,T[i])
            res[indx] = T[i]
            le[i] = len(res)
    return le

def lis(T):
    T2 = [T[i] for i in range(len(T))]
    res = lds(T2)
    res.reverse()
    return res
    
def mr( X ):
    inc1 = lis_nlogn(X)
    inc = lis(X)
    dis = lds(X)
    max_inc = max(inc1)
    max_dis = max(dis)
    max_mix = 0
    mix_indx = 0
    for i in range(len(X)-1):
        curr = dis[i] + inc[i+1]
        if curr > max_mix:
            max_mix = curr
            mix_indx = i
    
    print(max_mix)
    if max_inc > max_dis > max_mix:
        indx = inc1.index(max_inc)
        res = [X[indx]]
        for i in range(indx,-1,-1):
            if max_inc == 1:
                return res
            if X[i] > res[len(res)-1]:
                res.append(X[i])
                max_inc -= 1
    
    if max_dis > max_inc > max_mix:
        indx = inc.index(max_dis)
        res = [X[indx]]
        for i in range(indx,len(max_dis)):
            if max_dis == 1:
                return res
            if X[i] < res[len(res)-1]:
                res.append(X[i])
                max_dis -= 1
    
    res = [0 for _ in range(max_mix)]
    print(mix_indx)
    for i in range(mix_indx,-1,-1):
        if max_dis == 1:
                return res
        if X[i] > res[len(res)-1]:
            res.append(X[i])
            max_dis -= 1
    for i in range(mix_indx+1,len(inc)):
        if max_inc == 1:
                return res
        if X[i] > res[len(res)-1]:
            res.append(X[i])
            max_inc -= 1
    
    return res



    
runtests( mr )

# T = [1,10,5]

# print(mr(T))


