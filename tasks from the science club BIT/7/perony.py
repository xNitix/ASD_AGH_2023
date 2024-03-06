from queue import PriorityQueue

def perony(m,tab):
    n = len(tab)
    Que = PriorityQueue()
    
    for i in range(n):
        Que.put([tab[i],0])
        
    cnt = 0
    while not Que.empty():
        czas,rodzaj = Que.get()
        if rodzaj == 1:
            cnt -= 1
        else:
            cnt += 1
            if cnt > m:
                return False
            Que.put([[czas[1],czas[0]],1])
            
    return True


I_like_TRAINNSSS = [[7,10],[8,9],[9,10],[10,13],[11,13],[12,13]]

print(perony(3,I_like_TRAINNSSS))
