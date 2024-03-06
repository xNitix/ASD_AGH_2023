from queue import PriorityQueue
def peron(T,m):
    n = len(T)
    Que = PriorityQueue()
    for i in range(n):
        Que.put([T[i][0],1])
        Que.put([T[i][1],-1])
           
    cnt = 0
    
    while not Que.empty():
        per,co = Que.get()
        
        if co == 1:
            cnt+=1
        else:
            cnt -= 1
            
        if cnt > m:
            return False

    return True

T = [[0,1],[1,3],[2,3],[2,4],[3,4],[4,5],[4,5]]

print(peron(T,3))

