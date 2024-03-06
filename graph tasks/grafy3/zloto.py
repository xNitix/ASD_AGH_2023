from queue import PriorityQueue

def zloto(G):
    n = len(G)
    inf = float("inf")
    wagi = [-inf for _ in range(n)]
    Que=PriorityQueue()
    wagi[0] = 0
    parent = [None for _ in range(n)]
    Que.put([0,0])
    
    def relax(v,wagi,zloto_po):
        if wagi[v] < zloto_po:
            wagi[v] = zloto_po
            return True
        return False
            
    
    while not Que.empty():
        bak, u = Que.get()
        bak = abs(bak)
        for i in range (1,len(G[u])):
            zloto_w_u=G[u][0]
            waga,v = G[u][i][0],G[u][i][1]
            if v == -1:
                continue
            if (zloto_w_u - waga) >=  0:
                if zloto_w_u - waga > 10:
                    cur_bak = 10
                else:
                    cur_bak = zloto_w_u - waga
            else:
                cur_bak = zloto_w_u - waga
            if bak + cur_bak >= 0:
                zloto_po = bak + cur_bak
                if relax(v,wagi,zloto_po):
                    parent[v] = u
                    Que.put([-zloto_po,v])
                    
    return wagi
                    
G = [[8, [6,3],[4,2],[7,1]],
     [22, [1,2],[21,3],[0,-1]],
     [9, [11,3],[0,-1],[7,-1]],
     [15, [0,-1],[1,-1],[0,-1]]]     

print(zloto(G))          
            
        