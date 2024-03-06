# BFS - Breadth-First Search (przejscie grafu wszerz) imituje wrzucenie kamienia do wody, falowo przechodzimy do kolejnych wierzcholkow, dajemy do kolejki pierwszy wierzcholek nastepnie
# przechodzimy po jego sasiadach pod awrunkiem ze nie byly jeszcze odwiedzone, zmieniajacach ich visited na tru, zwiekszajac promien i zmieniajac parent, nsatepmnie dorzucamy je do kolejkki
# robimy tak do momentu gdy kolejka nie bedzie pusta, zastosowania :
# *1 znalezienie najktorzych sciezek miedzy dwoma punktami, dzieki tablicy d, jak znajdziemy to przerywamy i zwracamy aktualny promien
# *2 sprawdzenie spojnosci grafu, jesli po zakonczeniu algorytmu nie wszystko jest na true w visited to niespojny
# *3 dwudzielnosc, Początkowo wszystkie wierzchołki grafu powinny posiadać kolor neutralny. Wybieramy dowolny wierzchołek w grafie i kolorujemy go np. na czerwono. Następnie przechodzimy 
#  algorytmem BFS przez graf począwszy od wybranego wierzchołka kolorując po drodze wszystkich nie odwiedzonych sąsiadów na kolor przeciwny 
# *4 wykrywanie cykli jesli do kolejki dojdzie elemnt ktory juz na vizyted i nie jest rodzicem obecnego wierzcholka to jest cykl
# zlozonosc rep listow O(V+E), rep.macierzowa O(V^2)
from collections import deque

def BFS(G,s):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    d=[-1 for _ in range(n)]
    Queue=deque()
    Queue.append(s)
    visited[s]=True
    d[s]=0
    while len(Queue) != 0:
        u = Queue.popleft()
        print(u)
        for v in G[u]:
            if visited[v] == False:
                d[v]=d[u]+1
                parent[v]=u
                visited[v]=True
                Queue.append(v)
# *1
def BFS_Promien(G,s,k):
    n=len(G)
    visited=[False for _ in range(n)]
    d=[-1 for _ in range(n)]
    Queue=deque()
    Queue.append(s)
    visited[s]=True
    d[s]=0
    while len(Queue) != 0:
        u = Queue.popleft()
        for v in G[u]:
            if visited[v] == False:
                d[v]=d[u]+1
                visited[v]=True
                if v == k:
                    print(d[v])
                    return d[v]
                Queue.append(v)

# *2
def BFS_Czyspojny(G):
    n=len(G)
    visited=[False for _ in range(n)]
    s=0
    Queue=deque()
    Queue.append(s)
    visited[s]=True
    while len(Queue) != 0:
        u = Queue.popleft()
        print(u)
        for v in G[u]:
            if visited[v] == False:
                visited[v]=True
                Queue.append(v)
    for i in range(len(visited)):
        if visited[i] == False:
            return False
    return True

# *3 #zakladam ze graf jest pelny
def BFS_dwudzielnosc(G):
    n = len(G)
    s=0
    colors=[-1 for _ in range(n)]
    visited=[False for _ in range(n)]
    Que = deque()
    Que.append(s)
    colors[s]=1
    visited[s]=True
    while len(Que) != 0:
        u = Que.popleft()
        for v in G[u]:
            if colors[v] == -1:
                colors[v]=colors[u]%2 + 1
            if colors[v] == colors[u]:
                return False
            if visited[v] == False:
                Que.append(v)
                visited[v]=True
                   
    return True
        
# *4  
def BFS_cykl(G):
    n=len(G)
    s=0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    d=[-1 for _ in range(n)]
    Queue=deque()
    Queue.append(s)
    visited[s]=True
    d[s]=0
    while len(Queue) != 0:
        u = Queue.popleft()
        for v in G[u]:
            if visited[v] == True and v != parent[u]:
                return True
            if visited[v] == False:
                d[v]=d[u]+1
                parent[v]=u
                visited[v]=True
                Queue.append(v)
    return False
    
#G = [[1,6],[0,2],[1],[6,4],[3,5],[4],[0,3]]
#print(BFS_cykl(G))

# DFS - Depth-First search (przeszukiwanie w głąb) Tak więc podstawową ideą jest rozpoczęcie od korzenia lub dowolnego dowolnego węzła i zaznaczenie węzła i przejście do sąsiedniego
# nieoznaczonego węzła i kontynuowanie tej pętli, aż nie będzie żadnego nieoznaczonego sąsiedniego węzła. Następnie cofnij się i sprawdź inne nieoznaczone węzły i przejdź przez nie.
# zastosowanie : 
# *1 spójnosc - jesli w visited zostanie jakis false
# *2 dwudzielnosc - przypisywanie na przemian kolorow i patrzenie czy sie jakis nie pokryje z sasiadem
# *3 wykrywanie cykli - jesli trafimy na jakis ktory byl visited i nasz wierzcholerk nie jest jego rodzicem to jest cykl
# *4 sortowanie topologiczne - dag - directed ancyclic graph (skierowany graf acykliczny) uozenie jego wierzcholkow w takiej
# kolejnosci ze krawedzie wskazuja wylacznie z lewej na prawa. Uruchamiamy DFS i po przetworzeniu wierzcholka dodajemy go na pocatku listy
# *5 silne spojne skladowe - Wykonujemy DFS w grafie G, zapisując czasy przetworzednia. Odrwoc kierunek wszystkich krawędzi. Wykonaj DFS
# wyliczając wierzchołki w kolejności malejących czasów przetworzenia z poprzedniego wykonania. Wierzchołki odwiedzone w danym "DFSVisit"
# tworząsilnie spójne skłaowe
# *6 odtworzenie cyklu Eulera - Wykonujemy DFS, ale : po drodze usuwamy krawedzie po ktorych przeszlismy, do danego wierzcholka mozemy wejsc
# dowolna liczbe razy, po przetworzeniu danego wierzcholka dopisujemy go na poczatku tworzonego cyklu zlozonosc O(V+E), O(V^2)
# *7 mosty / punkty artykulacji  - wykonaj DFS, zapisz dla kazdego wierzcholka jego czas prztworzenia, do tablicy low zapisuj minimum z :
# low(source)=min(low[source],low[dizecka]) a jesli dany v byl juz visited to low(source)=min(low[source]time_visit[v]) jesli po wykonaniu
# DFS jakis wiercholek ma taki sam czas odwiedzenia i low i jego rodzic nie jest none to jest on wierzcholkiem mostu wraz z swoim rodzicem
# zlozonosc : rep.listowa O(V+E), rep.macierzowa O(V^2)
# *8 Cykl hamiltona - odwiedza kazdy wierzcholek dokladnie raz - Brut Force sprawdza O(V!) mozliwosci Nie da sie lepiej bo rozpoznawanie
# czy graf ma cykl hamiltiona to problem np trudny ( jest to tez algorytm znajdywania najdluzszej sciezki w grafie, wystarczy usunac 1 krawdz)

def DFS(G):
    n = len(G)
    time = 0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    
    def DFSVisit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        time +=1
        visited[u]=time
        for v in G[u]:
            if visited[v] == False:
                print(v)
                parent[v]=u
                DFSVisit(G,v)
    
    for i in range(len(G)):
        if visited[i] == False:
            print(i)
            DFSVisit(G,i)
            
# *2
def DFS_dwudzielnosc(G):
    n = len(G)
    time = 0
    visited=[False for _ in range(n)]
    color=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    flag = 0
    def DFSVisit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal color
        nonlocal parent
        nonlocal flag
        time +=1
        visited[u]=time
        if time == 1:
            color[u]=1
        else:
            color[u]=color[parent[u]] % 2 + 1
        for v in G[u]:
            if visited[v] != False and color[v] == color[u]:
                flag = 1
                return False 
            if visited[v] == False:
                parent[v]=u
                DFSVisit(G,v)
        time +=1
    
    for i in range(len(G)):
        if flag:
            return False
        if visited[i] == False:
            DFSVisit(G,i)
    return True

# *3
def DFS_cykle(G):
    n = len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    time = 0
    flag = 0
    def DFSVisit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        nonlocal flag
        time += 1
        visited[u] = time
        for v in G[u]:
            if visited[v] != False and v != parent[u]:
                flag = True
                return True
            if visited[v] == False:
                parent[v]=u
                DFSVisit(G,v)
        time+=1

    for i in range(n):
        if flag:
            return True
        if visited[i] == False:
            DFSVisit(G,i)
    
    return False

# *4 
def DFS_sort_topologiczne(G):
    n = len(G)
    time = 0
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    res = []
    
    def DFSVisit(G,u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        nonlocal res
        
        time +=1
        visited[u]=time
        
        for v in G[u]:
            if visited[v] == False:
                parent[v]=u
                DFSVisit(G,v)
                
        res.append(u)
        time +=1
    
    for i in range(len(G)):
        if visited[i] == False:
            DFSVisit(G,i)
            
    for i in range(len(res)-1,-1,-1):
        print(res[i])

# *5 silnie spojne skladowe 

def silnie_spojne(G):
    n = len(G)
    visited = [False for _ in range(n)]
    order = []

    def DFSVisit(G,s,visited,order : list ):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFSVisit(G,v,visited,order)
        order.append(s)
    
    for i in range(n):
        if not visited[i]:
            DFSVisit(G,i,visited,order)
            
    def Flip_Edge(G):
        n = len(G)
        G_C = [[] for _ in range(n)]
        for i in range(n):
            for v in G[i]:
                G_C[v].append(i)
        return G_C
    
    G2 = Flip_Edge(G)
    
    order.reverse()  
    
    visited = [False for _ in range(n)]
    res = []
    
    for i in order:
        components = []
        if not visited[i]:
            DFSVisit(G2,i,visited,components)
            res.append(components)
            
    for i in res:
        if len(i) == 1:
            return False
    
    return res

# *6
# reprezentacja macierzowa
def DFS_Euler(G,vertex,res):
    for i in range(len(G)):
        if G[vertex][i] == 1:
            G[vertex][i] = 0
            G[i][vertex] = 0
            DFS_Euler(G, i, res)
    res.append(vertex)

def DFS_Euler_path(G):
    # sprawdzam czy istnieje cykl eulera
    for i in range(len(G)):
        edges = 0
        for j in range(len(G[i])):
            if G[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return False
    
    res = [] 
    DFS_Euler(G,0,res)
    res.reverse()
    return res
# reprezenctacja listy sasiedztwa - tworzymy tablice visited 2wymiarowa
# nie dziala :(
def euler_list(G):
    n = len(G)
    res = []
    visited=[[False for _ in range(n)] for _ in range(n)]
    def DFS(G,parent,visited,res):
        for v in G[parent]:
            if visited[parent][v] == False:
                visited[parent][v] = 1
                visited[v][parent] = 1
                DFS(G,v,visited,res)
        res.append(v)
    
    DFS(G,0,visited,res)
    reversed(res)
    return res

# reprezentacja 
# *7
from math import inf
def bridge(G):
    n = len(G)
    visited=[False for _ in range(n)]
    parent_t=[None for _ in range(n)]
    time_vis=[0 for _ in range(n)]
    low = [inf for _ in range(n)]
    time = 0

    def DFS(G,parent,visited,parent_t,time_vis,low,time):
        visited[parent] = True
        time_vis[parent]=time
        time+=1
        low[parent]=time_vis[parent]
        for v in G[parent]:
            if visited[v] == False:
                parent_t[v]=parent
                DFS(G,v,visited,parent_t,time_vis,low,time)
                low[parent]=min(low[parent],low[v])
            elif parent_t[parent] != v:
                low[parent]=min(low[parent],time_vis[v])

    bridges = []
    for i in range(n):
        if visited[i] == False:
            DFS(G,i,visited,parent_t,time_vis,low,time)
    for i in range(n):
        if time_vis[i] == low[i] and parent_t[i] != None:
            bridges.append([parent_t[i],i])
    return bridges

# *8 
def permutacje(lista,indx):
    if indx < len(lista):
        for i in range(indx,len(lista)):
            lista[i],lista[indx]=lista[indx],lista[i]
            permutacje(lista,indx+1)
            lista[i],lista[indx]=lista[indx],lista[i]
    else:
        print(lista)

def hamilton(G):
    n = len(G)
    flaga=0
    res=[]
    lista=[ i for i in range(n)]
    def permutacje(G,lista,indx):
        if indx < len(lista):
            for i in range(indx,len(lista)):
                lista[i],lista[indx]=lista[indx],lista[i]
                permutacje(G,lista,indx+1)
                lista[i],lista[indx]=lista[indx],lista[i]
        else:
            nonlocal res
            flaga = 0
            for i in range(len(lista)-1):
                if G[i][i+1] == G[i+1][i] == 0:
                    flaga = 1
                    break
            if flaga == 0:
                res=lista
        return False
    permutacje(G, lista, 0)
    return res

Gham = [[0,1,1],
        [1,0,1],
        [1,1,0]]

#print(hamilton(Gham))

G1 = [[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[4,3],[0,2,7],[6]]
G = [[1,6],[0,2],[1,7,4],[6,4,7],[3,5,4],[4],[0,3,7],[6,2,3]]
G2 = [[0,1,1,0,0,0],
      [1,0,0,1,0,0],
      [1,0,0,0,0,1],
      [0,1,0,0,1,0],
      [0,0,0,1,0,1],
      [0,0,1,0,1,0]]
G3=[[1,2],
    [0,2,3,4,5,6],
    [0,1,3,4,5,6],
    [1,2,4,5],
    [1,2,3,5],
    [1,2,3,4],
    [1,2]
    ]

# print(G3)
# x=euler_list(G3)
# def listToMatrix(L):
#     n=len(L)
#     M=[[0 for _ in range(n)] for o in range(n)] 

#     for i in range(n):
#         for w in L[i]:
#             M[i][w]=1

#     return M
# z=DFS_Euler_path(listToMatrix(G3))
# print(x,z)

# Dijkstra macierzowa O (V^2)
from math import inf
def Dijkstra_m(G,s,k):
    n = len(G)
    wagi=[inf for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    
    wagi[s]=0
    
    while True:
        minimum=inf
        min_indx=0
        
        for i in range(n):
            if visited[i] == False:
                if wagi[i] < minimum:
                    minimum=wagi[i]
                    min_indx=i
                    
        if minimum == inf:
            break
        
        visited[min_indx]=True
        
        for u in range(len(G[min_indx])):
            if G[min_indx][u] == -1 or visited[u] == True:
                continue
            if wagi[min_indx] + G[min_indx][u] < wagi[u]:
                wagi[u]=wagi[min_indx] + G[min_indx][u]
                parent[u]=min_indx
                
    return wagi[k]
    
GM_D = [[-1,10,-1,30,100],
        [10,-1,50,-1,-1],
        [-1,50,-1,20,10],
        [30,-1,20,-1,60],
        [100,-1,10,60,-1]
        ]

#print(Dijkstra_m(GM_D,0,4))

# Dijkstra Lista sąsiedztwa (E*log(V))

from queue import PriorityQueue
def Dijksra_L(G,s,t):
    n = len(G)
    inf=float("inf")
    Que=PriorityQueue()
    wagi=[inf for _ in range(n)]
    parent=[None for _ in range(n)]
    wagi[s] = 0
    Que.put((0,s))
    
    while Que.qsize() != 0:
        nic,v = Que.get()
        for u,waga in G[v]:
            if wagi[v] + waga < wagi[u]:
                wagi[u] = wagi[v] + waga
                parent[u] = v
                Que.put((wagi[u],u))
    return wagi[t]
                
import heapq
def Dijksra_L_H(G,s,t):
    
    def relax(u,waga,v,wagi,Que):
        if wagi[u] > wagi[v] + waga:
            wagi[u] = wagi[v] + waga
            heapq.heappush(Que,(wagi[u],u))
        
    def Dijksra(G,s,t):
        n = len(G)
        Que=[]
        inf=float("inf")
        wagi=[inf for _ in range(n+1)]
        wagi[s] = 0
        heapq.heappush(Que,([0,s]))
        
        while len(Que) != 0:
            wag,v = heapq.heappop(Que)
            
            if v == t:
                return wagi[t]
            
            for u in G[v]:
                relax(u[0],u[1],v,wagi,Que)
                    
        return None
    
    return Dijksra(G,s,t)

GD=[[[4,100],[1,10],[3,30]],
    [[0,10],[2,50]],
    [[3,20],[4,10],[1,50]],
    [[2,20],[0,30],[4,60]],
    [[3,60],[0,100],[2,10]]]

#print(Dijksra_L_H(GD,0,3))

# Bellman-Ford - znajduje najkrotsza sciezke najkrótsze ścieżki z pojedynczego wierzchołka źródłowego do wszystkich innych wierzchołków 
# wliczajac w to ujemkne wagi, dijkstra nie wroci juz nigdy do punktu w ktorym byl, Bellman sprawdza kazda mozliwa odleglosc miedzy kazda para,
# wiec zawsze wroci odpowiddnia sciezke, nawet gdy np musimy isc po malejacych krawedziach, jesli po potrojnnym for
# wykonamy jeszcze raz proces relakasacji krawedzi i droga sie poprawki to oznacza ze mamy ujemny cykl
# Zlozonosc : O(V*E)

def Bellman_Ford(G,s):
    n = len(G)
    inf = float("inf")
    wagi = [inf for _ in range(n)]
    parents = [None for _ in range(n)]
    wagi[s] = 0
    
    def relax(u,v,wagi,edge):
        if wagi[v] > wagi[u] + edge:
            wagi[v] = wagi[u] + edge
            return True
        return False
    
    for _ in range(n-1):
        for u in range(n):
            for edge,v in G[u]:
                if relax(u,v,wagi,edge):
                    parents[v] = u
    # sprawdzanie czy ujemny cykl
    for u in range(n):
        for edge,v in G[u]:
            if relax(u,v,wagi,edge):
                return None
    
    return wagi,s
#    odleglosci,punkt    
  
  
# G = [[[-1,1],[4,2]],
#      [[3,2],[2,3],[2,4]],
#      [],
#      [[5,2],[1,1]],
#      [[-3,3]]]

# print(Bellman_Ford(G,0)) 

# Algorytm Floyda-Warschalla
# Znajduje wszystkie najkrótsze ścieżki pomiedzy każdą parą wierzchołków w grafie ważonym.( z dowlnego punktu do dowolnego wierzcholka)
# Wagi krawędzi mogą być zarówno dodatnie jak i ujemne, ale graf nie może posiadać ujemnych cykli.
# Złożoność: O(V^3)

def Floyd_Warschall(G):
    n = len(G)
    inf = float("inf")
    wagi = G[:]
    parents = [[None for _ in range(n)]for _ in range(n)]
    
    def relax(i,j,k,wagi):
        if wagi[j][k] > wagi[j][i] + wagi[i][k]:
            wagi[j][k] = wagi[j][i] + wagi[i][k]
            return True
        return False
    
    
    for i in range(n):
        for j in range(n):# startowy
            for k in range(n): # koncowy
                if relax(i,j,k,wagi):
                    parents[j][k] = i
                    
    # sprawdzanie ujemnego cyklu
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if relax(i,j,k,wagi):
                    wagi[j][k] = -inf
                    parents[j][k] = -1
    
    return wagi,parents
         

# Z definicji graf musi byc skierowany 

# Algorytm Prima do znalezienia MST (minimalne drzewo rospinajace)
# Implementacja dla list sąsiedztwa.
# Zlozonosc : O(E*log(V))

from queue import PriorityQueue
def prim(G):
    inf = float("inf")
    n = len(G)
    visited = [False for _ in range(n)]
    wagi = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    Que = PriorityQueue()
    wagi[0] = 0
    Que.put([wagi[0],0])
    
    while not Que.empty():
        _, u = Que.get()
        visited[u] = True
        for v,edge in G[u]:
            if not visited[v]:
                 if wagi[v] > edge:
                     wagi[v] = edge
                     parent[v] = u
                     Que.put([wagi[v],v])
    
    MST=[]
    for i in range(n):
        if parent[i] != None:
             MST.append([parent[i],i,wagi[i]])
    
    if len(MST) < n - 1:
        return False
    
    return MST


#def prim(G):
    inf = float("inf")
    n = len(G)

    p = PriorityQueue()
    p.put((0, 0))
    for i in range(1, n):
        p.put((inf, i))

    parents = [None] * n
    visited = [False] * n
    min_weight = [inf] * n

    min_weight[0] = 0

    while not p.empty():
        _, u = p.get()
        visited[u] = True

        for edge, v in G[u]:

            if not visited[v]:
                if min_weight[v] > edge:
                    min_weight[v] = edge
                    parents[v] = u
                    p.put((edge, v))

    MST = []
    for i in range(n):
        if parents[i] is not None:
            MST.append((parents[i], i, min_weight[i]))

    return MST


# Algorytm Kruskala do znalezienia MST (minimalnego drzewa rozpinającego)
# Algorytm wykorzystuje strukturę find-union.
# Implementacja dla reprezentacji poprzez listy sąsiedztwa.
# Zlozonosc : O(E*log(V))

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = self
        self.rank = 0


def findSet(x):
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent


def union(x, y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        y.parent = x

    elif y.rank > x.rank:
        x.parent = y

    else:
        x.parent = y
        y.rank += 1


def Kruskal(G):
    n = len(G)
    edges = []

    for u in range(len(G)):
        for edge, v in G[u]:
            edges.append((edge, u, v))

    edges.sort(key=lambda x: x[0])

    MST = []
    sets = [Node(i) for i in range(n)]

    # przechodzi po krawędziach i jeśli wierzchołki są w osobnych zbiorach (czyli nie ma połączenia między u a v) to dodaję krawędź do MST
    for edge, u, v in edges:
        if findSet(sets[u]) != findSet(sets[v]):
            MST.append((edge, u, v))
            union(sets[u], sets[v])

    return MST


# Algorytm Forda-Fulkersona znajdujący maksymalny przeplyw w grafie od wierzchołka s do t.

# Implementacja dla reprezentacji macierzowej.
from queue import Queue
# BFS, który sprawdza czy istnieje ścieżka z s do t i aktualizuje tablice parent
def BFS(G, s, t, parent):
    n = len(G)
    visited = [False] * n

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for i in range(n):
            # 0-brak krawędzi
            if G[u][i] != 0 and not visited[i]:
                parent[i] = u
                visited[i] = True
                q.put(i)

    return visited[t]


def fordFulkerson(G, s, t):
    n = len(G)
    parent = [False] * n
    maxFlow = 0

    # dopóki istnieje ścieżka z s do t
    while BFS(G, s, t, parent):
        u = t
        mini = float("inf")

        # szukam najmniejszej krawędzi na ścieżce z s do t
        while u != s:
            mini = min(mini, G[parent[u]][u])
            u = parent[u]

        # wartość przepływu zwiększam o wagę najmniejszej krawędzi na ścieżce z s do t
        maxFlow += mini

        u = t

        # aktualizuje wartosci krawędzi
        while u != s:
            G[parent[u]][u] -= mini
            G[u][parent[u]] += mini
            u = parent[u]

    return maxFlow

G = [[0,6,3,0],
     [0,0,2,4],
     [0,0,0,1],
     [0,0,0,0],]

print(fordFulkerson(G,0,3))
    