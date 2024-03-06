# Norbert Dziwak
# uzywam algorytmu Dijkstry z romznaznymi podwojnie wierzcholkami, jeden z nich odpowiada
# za sytuacje gdy do danego wierzcholka weszlismy nie robiac jeszcze do tej pory napadu
# druga jesli weszlismy do zwierzcholka z juz wykonanym rabunkiem, albo wykonamy rabunek w nim.
# jesli weszlismy bez rabunku to mozemy albo isc dalej nie rabujac go (relaxN) ablo 
# dokonujac rabunku w tym wierzcholku(relaxR). gdy wchodzi do wierzcholka z juz wykonanym
# wczesniej rabunkiem to zostaje nam tylko moliwosc isc dalej z popelnionym juz rabunkiem (relaxP)
# Złożoność : V^2logv - dijkstra rozmnozone wierzcholki
from egz1Atesty import runtests
from queue import PriorityQueue

def gold1(G,V,s,t,r):

  def dijkstra(G,V,s,t,r):
    n = len(G)
    inf = float("inf")
    wagi = [- inf for _ in range(n*2)]
    visited = [False for _ in range(n*2)]
      
    Que = PriorityQueue()
    wagi[s] = 0
    wagi[s + n] = V[0]
    
    visited[s] = True
    visited[s+n] = True
      
    Que.put([0,'N',s,V[0]])
    Que.put([0,'R',s+n,0])
      
    def relaxN(u,v,wagi,how,edge):
        if wagi[v + how] < wagi[u] - edge:
            wagi[v + how] = wagi[u] - edge
            return True
        return False
      
    def relaxR(u,v,wagi,how,edge,r,V):
        if wagi[v + how] < wagi[u] + V[v] - edge:
            wagi[v + how] = wagi[u] + V[v] - edge
            return True
        return False

    def relaxP(u,v,wagi,how,edge,r,V):
        if wagi[v + how] < wagi[u] - 2*edge - r:
            wagi[v + how] = wagi[u] - 2*edge - r
            return True
        return False

      
    while not Que.empty():
        _,how,u,left = Que.get()
        for v,edge in G[u%n]:
            if how == 'N':
                # idziemy dalej
                if not visited[v] and relaxN(u,v,wagi,0,edge):
                  visited[v] = True
                  Que.put([wagi[v],'N',v,V[v]])

                # napadamy
                if not visited[v+n] and relaxR(u,v,wagi,n,edge,r,V):
                  visited[v+n] = True
                  Que.put([wagi[v + n],'R',v + n,0])

            if how == 'R':
                # idziemy dalej
                if not visited[v+n] and relaxP(u,v,wagi,n,edge,r,V):
                  visited[v+n] = True
                  Que.put([wagi[v + n],'R',v + n,V[v]])
            
    a = wagi[t]
    b = wagi[t - n]
    if b > 0:
      return -b
    a = abs(a)
    b = abs(b)
    return min(a,b)

  return dijkstra(G,V,s,t,r)

def gold(G,V,s,t,r):
    
    def dijkstra(G,s,t,r,p):
      inf = float("inf")
      visited = [False for _ in range(len(G))]
      cost = [inf for _ in range(len(G))]
      Que = PriorityQueue()
      cost[s] = 0
      Que.put([0,s])
      
      def relax(u,v,edge,r):
        if cost[v] > cost[u] + edge*p + r:
          cost[v] = cost[u] + edge*p + r
          return True
        return False
      
      while not Que.empty():
        _,u = Que.get()

        visited[u] = True
        for v,edge in G[u]:
          if not visited[v]:
            if relax(u,v,edge,r):
              Que.put([cost[v],v])
              
      return cost
    
    mini = dijkstra(G,s,t,0,1)
    maxi = dijkstra(G,t,s,r,2)
    
    inf = float("inf")
    res = inf
    
    for i in range(len(G)):
      res = min(res,mini[i] + maxi[i] - V[i])

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
