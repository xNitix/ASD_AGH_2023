from queue import PriorityQueue

def lake_count(G):
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    visited = [[False for _ in range(len(G[0]))]for _ in range(len(G))]
    lake_count = 0
    
    curr_deep = 1
    
    def in_matrix(G,x,y):
        max_y = len(G)
        max_x = len(G[0])
        return 0 <= x < max_x and 0 <= y < max_y
        
    def Dfs_macierz(G,x,y,visited,moves):
        nonlocal curr_deep
        visited[y][x] = curr_deep
        for i in range(4):
            x1 = x + moves[i][0]
            y1 = y + moves[i][1]
            if in_matrix(G,x1,y1) and not visited[y1][x1] and G[y1][x1] == "W":
                curr_deep += 1
                Dfs_macierz(G,x1,y1,visited,moves)
        
    for i in range(len(G)):
        for j in range(len(G[i])):
            if not visited[i][j] and G[i][j] == 'W':
                curr_deep = 1
                Dfs_macierz(G,j,i,visited,moves)
                lake_count += 1
    deep = 0
    
    for i in range(len(G)):
        for j in range(len(G[i])):
            deep = max(deep,visited[i][j])  
    
    inf = float("inf")
    Que = PriorityQueue()
    cost = [[inf for _ in range(len(G[0]))]for _ in range(len(G))]
    cost[0][0] = 0
    Que.put([0,0,0]) # cost | x | y
    
    def relax(x1,y1,x,y):
        if cost[y1][x1] > cost[y][x] + 1:
            cost[y1][x1] = cost[y][x] + 1
            return True
        return False
    
    while not Que.empty():
         _, x, y = Que.get()
         visited[y][x] = True
         
         if x == y == len(G)-1:
            break
             
         for i in range(4):
            x1 = x + moves[i][0]
            y1 = y + moves[i][1]
            if in_matrix(G,x1,y1) and G[y1][x1] == 'L' : 
                if relax(x1,y1,x,y):
                    Que.put([cost[y1][x1],x1,y1])
    
    return lake_count,deep,cost[len(G)-1][len(G)-1]

G = [['L','W','L','L','L','L','L','L'],
     ['L','W','L','W','W','L','L','L'],
     ['L','L','L','W','W','L','W','L'],
     ['L','W','W','W','W','L','W','L'],
     ['L','L','W','W','L','L','L','L'],
     ['L','W','L','L','L','L','W','W'],
     ['W','W','L','W','W','L','W','L'],
     ['L','L','L','W','L','L','L','L']
     ] 

print(lake_count(G))