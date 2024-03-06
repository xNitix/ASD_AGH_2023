from queue import Queue

def BFS(G,days):
    n = len(G)
    Que = Queue()
    Que.put([0,0])
    visited = [False for _ in range(n)]
    visited[0] = True
    
    while not Que.empty():
        u,day = Que.get()
        days[day]+=1
        
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Que.put([v,day+1])
    
def letter(G):
    n = len(G)
    days = [0 for _ in range(n+1)]
    BFS(G,days)
    max_per = max(days)
    day = days.index(max_per)
    return day
                    
G = [
    [1,2,3],
    [0,10,8,9,6],
    [0,7,6],
    [0,4,5],
    [3],
    [3,7],
    [2,1,9],
    [2,5],
    [9,1,10],
    [1,8,6],
    [1,8]
]

print(letter(G))
    