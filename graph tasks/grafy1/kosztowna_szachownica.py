# kosztowna szachownica - Dana jest szachownica o wymiarach n x n. Kazde pole (i.j) ma koszt (liczbe ze zbioru {1.....5)) umieszezony w tablicy A (na polu A(j](i]).
# W lewym górnym rogu szachownicy stoi król, którego zadaniem jest przejse do prawego dolnego rogu, przechodzac po polach o minmalnym sumarycznym koszcie. 
# Prosze zaimplementowac funkeje kings_path (A), która oblicza koszt sciezki króla. Funkcja powinna bye mozliwie jak najszybsza.
# Wykonuje algorytm Dijkstry gdzie jako kolejne wierzcholki do kolejki dodaje mozliwe ruchy krola z danego pola
# zlozonosc : O(ElogV) - zlozonosc dijkstry dla rep.lsitowej z kopcem binarnym

from queue import PriorityQueue
def kings_path(A):
    n = len(A)
    inf = float("inf")
    moves = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    visited = [[False for _ in range(n)]for _ in range(n)]
    cost = [[inf for _ in range(n)]for _ in range(n)]
    cost[0][0] = A[0][0]
    Que=PriorityQueue()
    Que.put([cost[0][0],0,0])
    visited[0][0]=True
    
    while Que.qsize() != 0:
        waga,w,k = Que.get()
        visited[w][k] = True
        if (w == n-1) and (k == n-1):
            break
        for x,y in moves:
            if (0 <= w + x < n) and ( 0 <= k + y < n) and not visited[w+x][k+y]:
                if cost[w+x][k+y] > cost[w][k] + A[w+x][k+y]:
                    cost[w+x][k+y] = cost[w][k] + A[w+x][k+y]
                    Que.put([cost[w+x][k+y],w+x,k+y])
    
    return cost[n-1][n-1]

G = [[6, 2, 111, 35, 7],
[1, 7, 21, 8, 1],
[7, 57, 51, 65, 3],
[5, 20, 76, 5, 65],
[9, 5, 5, 87, 9]]

print(kings_path(G))
    