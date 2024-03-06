from zad2testy import runtests
from queue import PriorityQueue


def robot(L, A, B):
    dl_r = len(L[0])
    dl_c = len(L)
    inf = float("inf")
    # (([0,1,2]rozne rozpedzenia)x4-rozne kierunki z ktorych przyszlismy)x dl_r x dl _c -> wszytki wierzcholki (macierz)
    dp = [[[[inf for _ in range(3)]for _ in range(4)]for _ in range(dl_r)]for _ in range(dl_c)]
    dp[A[1]][A[0]][0][0] = 0
    
    directions = [[1,0],[0,-1],[-1,0],[0,1]] # prawo,gora,lewo,dol - z kadego kierunku mozliwe sa zmianyt na o 1 lub 3 indeksy dalej %4
    speeds = [60,40,30]
    
    Que = PriorityQueue()
    
    Que.put([0,A[0],A[1],0,0]) # czas do tej pory(koszt)| x | y | zwrot | predkosc
    
    def relax(x,y,direct,speed,direct2,speed2,cost):
        x2 = x + directions[direct2][0]
        y2 = y + directions[direct2][1]
        if dp[y2][x2][direct2][speed2] > dp[y][x][direct][speed] + cost + speeds[speed2]:
            dp[y2][x2][direct2][speed2] = dp[y][x][direct][speed] + cost + speeds[speed2]
            return True
        return False
            
    while not Que.empty():
        time,x,y,direc,speed = Que.get()
        
        if (x,y) == B:
            return time
        
        # prawo (+3)
        if L[y+directions[(direc+3)%4][1]][x+directions[(direc+3)%4][0]] != 'X':
            if relax(x,y,direc,speed,(direc+3)%4,0,45):
                direct2 = (direc+3)%4
                x2 = x + directions[direct2][0]
                y2 = y + directions[direct2][1]
                Que.put([dp[y2][x2][direct2][0],x2,y2,direct2,0])
        
        # lewo (+1)
        if L[y+directions[(direc+1)%4][1]][x+directions[(direc+1)%4][0]] != 'X':
            if relax(x,y,direc,speed,(direc+1)%4,0,45):
                direct2 = (direc+1)%4
                x2 = x + directions[direct2][0]
                y2 = y + directions[direct2][1]
                Que.put([dp[y2][x2][direct2][0],x2,y2,direct2,0])
                
        # prosto
        if L[y+directions[direc][1]][x+directions[direc][0]] != 'X':
            if x == A[0] and y == A[1]:
                speed2 = 0
            else:
                speed2 = min(speed+1,2)
            if relax(x,y,direc,speed,direc,speed2,0):
                direct2 = direc
                x2 = x + directions[direct2][0]
                y2 = y + directions[direct2][1]
                Que.put([dp[y2][x2][direct2][speed2],x2,y2,direct2,speed2])
    
runtests( robot )




