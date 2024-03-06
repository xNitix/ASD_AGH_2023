# Najkrótsze Sciezki - Prosze zaimplementowaé algorytm BFS tak, aby znajdowalnajkrotsze 
# Sciezki w grafie i nastepnie, zeby dalo sie wypisac najkrotsza Sciezke z zadanego punktu 
# startowego do wskazanego wierzcholka.
# Wykonujemy algorytm BFS, w momnencie gdy trafimy na wierzcholek ktory jest naszym targetem
# przerywamy go i odtwarzamy sciezke dzieki przeskakiwaniu po rodzicach
# Zlozonosc obliczeniowa = O(V+E) - algorytm BFS 

from queue import Queue
def shortest_path_to(G,s,t):
    n = len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    odl=[-1 for _ in range(n)]
    res=[]
    Que=Queue()
    Que.put(s)
    visited[s]=True
    odl[s]=0
    
    flag = 0
    while Que.qsize() != 0:
        u=Que.get()
        if flag:
            break
        for v in G[u]:
            if not visited[v]:
                Que.put(v)
                visited[v] = True
                parent[v] = u
                odl[v] = odl[u] + 1
            if v == t:
                flag = 1
                break
    
    par = parent[t]
    while par != None:
        res.append(par)
        par=parent[par]
    res.reverse()
    res.append(t)
    return res

G=[[1,2],
   [0,4],
   [0,3,5],
   [4,2],
   [1,5,3],
   [6,4,2],
   [5,7],
   [6]]

print(shortest_path_to(G,0,3))
    