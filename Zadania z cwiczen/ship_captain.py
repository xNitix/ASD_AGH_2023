# Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden).
# Robimy zmodyfikowanawego BFS ktory bedzie szedl dalej tylko po mozliwej siatce ruchow tylko gdy glebokosc
# na to pozowli 
# Zloznonosc BFS macierzowego O(V^2)
from queue import Queue
def ship(G,t):
    nw = len(G)
    nk = len(G[0])
    moves = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    visited = [[False for _ in range(nk)]for _ in range(nw)]
    Que = Queue()
    visited[0][0] = True
    Que.put([0,0])
    while Que.qsize() != 0:
         w,k = Que.get()
         if (w == nw - 1) and (k == nk -1):
             return True
         for x,y in moves:
             new_w = w+x
             new_k = k+y
             if (0 <= new_w < nw) and (0 <= new_k < nk):
                 if G[new_w][new_k] > t and not visited[new_w][new_k] :
                     Que.put([new_w,new_k])
                     visited[new_w][new_k] = True
    return False
                    
             
