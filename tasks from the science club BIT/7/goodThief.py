def goodThief(A,n):
    max_money = [0 for _ in range(n)]
    max_money[0] = A[0]
    if A[1] > A[0]:
        max_money[1] = A[1]
    else:
        max_money[1] = A[0]
        
    for i in range(2,n):
        max_money[i] = max(max_money[i-2]+A[i],max_money[i-1])
    
    return max_money
    
    
T = [2,7,8,2,5,6,9,10,4,6,6]

print(goodThief(T,11))