from kol2btesty import runtests
from queue import PriorityQueue

def min_cost( O, C, T, L ):
    n = len(O)
    stacje = []
    for i in range(n):
        stacje.append([O[i],C[i]])
    stacje.append([0,0])
    stacje.append([L,0])
    stacje.sort()
    n_w = n+2
    inf = float('inf')
    min_a = [inf for _ in range(n_w)]
    min_a[0] = 0
    Quea=PriorityQueue()
    
    last_min = [0,0]
    #print(stacje)
    for i in range(1,n_w):
        while stacje[i][0] > last_min[1] + T and not Quea.empty(): 
            last_min = Quea.get()
        
        min_a[i] = last_min[0] + stacje[i][1]
        Quea.put([min_a[i],stacje[i][0]])
        
    min_b = [inf for _ in range(n_w)]
    min_b[n_w-1] = 0
    Queb=PriorityQueue()
    
    last_min = [0,L]
    
    for i in range(n_w-2,-1,-1):
        #print(stacje[i][0],last_min[1] - T)
        while stacje[i][0] < last_min[1] - T and not Queb.empty(): 
            last_min = Queb.get()
        
        min_b[i] = last_min[0] + stacje[i][1]
        Queb.put([min_b[i],stacje[i][0]])
        
    res = inf
    Quer = PriorityQueue()
    
    last_min=[0,0]
    for i in range(1,n_w):
        while stacje[i][0] > last_min[1] + 2*T and not Quer.empty():
            last_min = Quer.get()
            
        res = min(res,last_min[0] + min_b[i])
        Quer.put([min_a[i],stacje[i][0]])
        
    return res
    
            
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

print(min_cost(O,C,T,L))