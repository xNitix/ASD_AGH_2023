from zad1testy import runtests
from queue import PriorityQueue

def zbigniew( A ):
    inf = float("inf")
    n = len(A)
    energy = 0
    stops = 0
    last_indx = 0
    energy += A[0]
    A[0] = 0
    Que = []
    for i in range(1,n-1):
        Que.append([-A[i],-i])
    Que.append([-inf,-(i+1)])
    Que.sort()

    i = 0
    while len(Que) > 0:
        if i == len(Que):
            return -1
        
        snack,indx = Que[i]
        snack = -snack
        indx = -indx
        
        if indx > last_indx:
            if energy - (indx - last_indx) >= 0:
                if snack == inf:
                    return stops + 1
                energy += snack - (indx - last_indx) 
                stops += 1
                last_indx = indx
                Que.remove([-snack,-indx])
                i = 0
            else:
                i+=1
        else:
            energy += snack
            stops += 1
            Que.remove([-snack,-indx])
            i = 0

runtests( zbigniew ) 
