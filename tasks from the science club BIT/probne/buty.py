from queue import PriorityQueue

def buty(G,x,y):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n*3)]
    parents = [None for _ in range(n*3)]
    Que = PriorityQueue()
    wagi[x] = 0
    
    Que.put([0,0,'A',0])
    
    def relax(u,v,wagi,way,edge):
        if way == 'C':
            if wagi[v + n] > wagi[u + 2*n] + edge:
                wagi[v + n] = wagi[u + 2*n] + edge
                return True
            return False
        elif way == 'A1':
            if wagi[v] > wagi[u] + edge:
                wagi[v] = wagi[u] + edge
                return True
            return False
        elif way == 'A2':
            if wagi[v + 2*n] > wagi[u]:
                wagi[v + 2*n] = wagi[u] 
                return True
            return False
        elif way == 'B':
            if wagi[v] > wagi[u + n] + edge:
                wagi[v] = wagi[u + n] + edge
                return True
            return False

          
    while not Que.empty():
        _,u,way,last = Que.get()
        for edge,v in G[u%n]:
            if way == 'A':
                #A
                if relax(u,v,wagi,'A1',edge):
                    parents[v + 0] = u
                    Que.put([wagi[v+0],v,'A',0])
                #C
                if relax(u,v,wagi,'A2',edge):
                    parents[v + 2*n] = u
                    Que.put([wagi[v+2*n],v,'C',edge])
                  
            if way == 'B':
                #A
                if relax(u,v,wagi,'B',edge):
                    parents[v + 0] = u
                    Que.put([wagi[v+0],v,'A',0])
            
            if way == 'C':
                #B
                kraw = max(edge,last)
                if relax(u,v,wagi,'C',kraw):
                    parents[v + n] = u
                    Que.put([wagi[v+n],v,'B',0])
    # for i in range(3):
    #     for j in range(n):
    #         print(wagi[j+i*n],end=' ')
    #     print('\n')
    
    wyn = 0 
    x = 0
    if wagi[n-1] < wagi[n-1 + n]:
        wyn = wagi[n-1]
        x = n - 1
    else:
        wyn = wagi[n-1 + n]
        x = n - 1 + n

    # print(x)
    # p = parents[x]
    # rodzice = []
    # while p != None:
    #     rodzice.append(abs(p-n))
    #     p = parents[p]
    return wyn       

        

G = [[[1,1]],
     [[1,2],[1,0]],
     [[7,3],[1,1]],
     [[8,4],[7,2]],
     [[8,3]]]

print(buty(G,0,4))

                
