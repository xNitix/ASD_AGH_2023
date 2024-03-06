# Wyscigi - Król Bitoeji postanowil zorganizowac serie wyScigów samochodowych. Wyscigi
# maja sie odbywac po trasach zamknietych, skladajaeych sie z odcinków autostrady laczacych miasta Bitoeji
# Król chce, zeby kade miasto bylo zaangazowane w dokladnie jeden wyscig. W tym celu nalezy sprawdzic,
# czy da sic wynajac odpowiednie odcinki autostad. Nalezy jednak pamictac o nastepujacych ograniczeniach:
# 1. w Bitocji wszystkie autostrady sa jednokierunkowe,
# 2. Z kandego miasta wychodza co najwyzej dwa odeinki autostrady.którymi mozna przyjechac z innych miast
# 3. do kazdego miasta dochodza co najwyzej dwa odcinki autostrady, którymi mozna przyjechac z innych miast
# Prosze zaproponowac algorytm, Aktóry majac na wejsciu opis sieci autostrad Bitocji sprawdza czy da sie
# zorganizowac serie wyscigow tak, zeby prez kazde miasto przebiegala trasa dokladnie jednego.
# Utrudnienie: Kazdy odcinek autostrady ma predzial dopuszczalnych cen i nalezy wybrac wspolna cene
# da wszystkich wynajetch odcinkow.

def wyscig(G):
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
    
    return True
                          
G = [[1],
     [2],
     [3],
     [0],
     [2,5],
     [6],
     [7],
     [5,4]]

print(wyscig(G))
