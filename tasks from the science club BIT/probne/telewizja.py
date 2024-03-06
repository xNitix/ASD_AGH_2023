def jebac_tvp(T,S,O):
    n = len(T)
    new_Tab = []
    for i in range(n):
        new_Tab.append([T[i][0],T[i][1],S[i]])
        
    new_Tab.sort(key=lambda x:x[1])
    new_Tab.sort(key=lambda x:x[0])
    
    money = [new_Tab[i][2]for i in range(n)]
    money[0] = new_Tab[0][2]
    
    for i in range(1,n):
        for j in range(i):
            if new_Tab[i][0] > new_Tab[j][1]:
                money[i] = max(money[i],money[j]+new_Tab[i][2])
    return max(money)

T = [ (0, 3), (4, 5), (1, 4), (1, 3)]
S = [ 5000, 3000, 17000, 15000 ]
O = 10

print(jebac_tvp(T,S,O))
