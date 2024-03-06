def profit (T):
    n = len(T)
    money = [0 for _ in range(n)]
    
    money[0] = T[0]
    money[1] = max(T[0],T[1])
    
    for i in range(2,n):
        money[i] = max(money[i-1],money[i-2] + T[i])
        
    is_cut=[False for _ in range(n)]
    
    if money[n-1] == money[n-3] + T[n-1]:
        is_cut[n-1] = True
    
    for i in range(n-2,1,-1):
        if money[i] == money[i-2] + T[i] and is_cut[i+1] == False:
            is_cut[i] = True
        
    if is_cut[2]:
        is_cut[0] = True
    else:
        if T[1] > T[0]:
            is_cut[1] = True
        else:
            is_cut[0] = True
    
    res=[]
    for i in range(n):
        if is_cut[i]:
            res.append(i)
            
    return res,money[n-1]

Forest = [1,5,1,0,1,3,9,1]

print(profit(Forest))
    
            
    