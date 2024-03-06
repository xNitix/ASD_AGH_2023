# zamieniamy na dowolne waluty

def change(x,money):
    n = len(money)
    inf = float("inf")
    cost = [inf for _ in range(x+1)]
    cost[0] = 0
    
    for i in range(n):
        cost[money[i]] = 1
    
    for i in range(1,x+1):
        for j in range(1,i):
            cost[i] = min(cost[i],cost[j] + cost[i-j])
            
    print(cost)
    return cost[x]

money = [1,2,7,10]
x = 54

print(change(x,money))
    