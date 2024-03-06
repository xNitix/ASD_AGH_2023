# Dane : A[0],...,A[n-1] - tablica liczb
# Zadanie : znalezc najdluzszy rosnacy podciag ( niekoniecznie spojny )
# 1.stworzenie obliczanej funkcji : 
# F(i) - funkcja obliczajaca najdluzszy podciag rosnacy konczacy sie na A[i]
# 2. Zapisanie funkcji w postaci rekurencji :
# F(0) = 1
# F(i) = max z F(t) gdzie t < i oraz A[t] < A[i]
# 3. Implementacja (z odtworzeniem sciezki): 

def pod_ciag(A):
    n = len(A)
    F = [1 for _ in range(n)]
    Path = [-1 for _ in range(n)]
    
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                Path[i] = j
    
    def path(A,P,i):
        if P[i] != -1:
            path(A,P,P[i])
        print(A[i])
        
    maxi = 0
    indx = 0
    for i in range(n):
        if maxi < Path[i]:
            maxi = Path[i]
            indx = i
    
    path(A,Path,indx)
    
    return maxi
        
A = [2,1,4,3,1,5,2,7,8,3]

pod_ciag(A)
        