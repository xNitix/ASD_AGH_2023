from queue import PriorityQueue

def islands(G,X,Y):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n*(3))]
    parents = [None for _ in range(n*(3))]
    Que = PriorityQueue()
    for i in range(3):
        wagi[X + i*n] = 0
    Que.put([0,'N',X])
    
    def relax(u,v,wagi,trans1,trans2,val):
        if trans1 == 'A' or trans1 == 'N':
            if wagi[v + trans2*n ] > wagi[u] + val:
                wagi[v + trans2*n ] = wagi[u] + val
                return True
            return False
        if trans1 == 'B':
            if wagi[v + trans2*n ] > wagi[u] + val:
                wagi[v + trans2*n ] = wagi[u] + val
                return True
            return False
        if trans1 == 'C':
            if wagi[v + trans2*n ] > wagi[u] + val:
                wagi[v + trans2*n ] = wagi[u] + val
                return True
            return False
        
        
    while not Que.empty():
        _,trans,u = Que.get()
        v = 0
        for indx in G[u%n]:
            if indx == 8 and trans != "C":
                if relax(u,v,wagi,trans,2,8):
                    parents[v + 2*n] = u
                    Que.put([wagi[v + 2*n],'C',v + 2*n])
            if indx == 5 and trans != "B":
                if relax(u,v,wagi,trans,1,5):
                    parents[v + 1*n] = u
                    Que.put([wagi[v + 1*n],'B',v + 1*n])
            if indx == 1 and trans != "A":
                if relax(u,v,wagi,trans,0,1):
                    parents[v + 0*n] = u
                    Que.put([wagi[v + 0*n],'A',v + 0*n])
            v+=1

    mini = inf
    ind = 0
    for i in range(3):
        if mini > wagi[Y + i*n]:
            mini = wagi[Y + i*n]
            ind = Y + i*n
    path=[]
    path.append(ind % n)
    p = parents[ind % n]
    while p != None:
        path.append(p % n)
        p = parents[p]
    path.reverse()

    wagi_w=[[]for i in range(n)]
    for i in range(n):
        wagi_w[i].append(wagi[i])
    for i in range(n):
        wagi_w[i].append(wagi[i+n])
    for i in range(n):
        wagi_w[i].append(wagi[i+2*n])
        
    return mini,path,wagi_w                                       
        

G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 8, 0, 8],
     [0, 0, 8, 1, 0, 5, 0]]
print(islands(G, 5, 2))