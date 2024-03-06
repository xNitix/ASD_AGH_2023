from queue import PriorityQueue

def paths(G,s,t):
    n = len(G)
    inf = float("inf")
    cos_s_t = [inf for _ in range(n)]
    cos_t_s = [inf for _ in range(n)]
    
    def dijkstra(s,t,ver):
        Que = PriorityQueue()
        if ver == 1:
            cos_s_t[s] = 0
            Que.put([0,s])
        else:
            cos_t_s[s] = 0
            Que.put([0,s])
        
        def relax(u,v,edge,ver):
            if ver == 1:
                if cos_s_t[v] > cos_s_t[u] + edge:
                    cos_s_t[v] = cos_s_t[u] + edge
                    Que.put([cos_s_t[v],v])
                    return True
                return False
            else:
                if cos_t_s[v] > cos_t_s[u] + edge:
                    cos_t_s[v] = cos_t_s[u] + edge
                    Que.put([cos_t_s[v],v])
                    return True
                return False
        
        while not Que.empty():
            _,u = Que.get()
            
            if u == t:
                return 
            
            for v,edge in (G[u]):
                relax(u,v,edge,ver)
    
    dijkstra(s,t,1)
    dijkstra(t,s,2)
    
    cnt = 0
    for i in range(n):
        for v,edge in G[i]:
            if i < v:
                if cos_s_t[i] + cos_t_s[v] + edge == cos_s_t[t]:
                    cnt += 1
                if cos_s_t[v] + cos_t_s[i] + edge == cos_s_t[t]:
                    cnt += 1
                
    return cnt

G = [ [(1,2), (2,4)],
      [(0,2), (3, 11), (4, 3)],
      [(0,4), (3,13)],
      [(1, 11), (2,13), (5, 17), (6, 1)],
      [(1,3), (5,5)],
      [(3,17), (4,5), (7,7)],
      [(3,1), (7,3)],
      [(5,7), (6,3)] ]
s = 0
t = 7

print(paths(G,s,t))