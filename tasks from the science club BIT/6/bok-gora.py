def matrix(T):
    n_w = len(T)
    n_k = len(T[0])
    inf = float("inf")
    
    cost = [[inf for _ in range(n_k)]for _ in range(n_w)]
    cost[0][0] = T[0][0]
    
    def in_matrix(n_w,n_k,x,y):
        return 0 <= x < n_k and 0 <= y < n_w
    
    for i in range(1,n_k):
        cost[0][i] = cost[0][i-1] + T[0][i]
        
    for i in range(1,n_w):
        cost[i][0] = cost[i-1][0] + T[i][0]
        
    for i in range(1,n_w):
        for j in range(1,n_k):
            cost[i][j] = min(cost[i][j-1],cost[i-1][j]) + T[i][j]
    
    print(*cost,sep='\n')
    
    return cost[n_w-1][n_k-1]

T = [[0 ,23 ,41 ,546,8 ],
     [34,234,416,546,8 ],
     [9 ,23 ,417,546,8 ],
     [10,235,641,546,8 ],
     [0 ,2  ,441,6  ,98]]

print("wynik : ",matrix(T))