def to_remove(B):
    n = len(B)
    high = [1 for _ in range(n)]
    parents = [None for _ in range(n)]
    
    for i in range(n):
        for j in range(i):
            if B[i][0] >= B[j][0] and B[i][1] <= B[j][1]:
                if high[i] < high[j] + 1:
                    high[i] = high[j] + 1
                    parents[i] = j
    
    inf = float("inf")
    
    max = -inf
    max_indx = 0
    for i in range(n):
        if max < high[i]:
            max = high[i]
            max_indx = i
            
    tower = []
    tower.append(max_indx)      
    parent = parents[max_indx]
    
    while parent != None:
        tower.append(parent)
        parent = parents[parent]
        
    not_in_tower = []
    for i in range(n):
        flag = 1
        for j in range(len(tower)):
            if i == tower[j]:
                flag = 0
        if flag:
            not_in_tower.append(i)
                
    return n - max, not_in_tower

Bricks = [[5, 10], [0, 5], [0, 2], [2, 6], [2, 6], [4, 10], [2, 10], [2, 9], [4, 5], [4, 5]]

print(to_remove(Bricks))