from kol1testy import runtests
#O(np)
# def particion(T,p,k):
#     i = p-1
#     x = T[k]
#     for j in range(p,k):
#         if T[j] <= x:
#             i+=1
#             T[j],T[i] = T[i],T[j]
#     i += 1
#     T[i],T[k] = T[k],T[i]
#     return i
            

# def Quick_select(T,p,n,i):
#     x = particion(T,p,n)
#     if x == i:
#         return T[x]
#     if x < i:
#         return Quick_select(T,x+1,n,i)
#     if x > i:
#         return Quick_select(T,p,x-1,i)
    
    

# def ksum(T, k, p):
#     n = len(T)
#     suma = 0
#     for i in range(n-p+1):
#         new_T = T[i:i+p]
#         curr = Quick_select(new_T,0,len(new_T)-1,len(new_T)-k)
#         suma+=curr
#     return suma

# nlogn - dwa kopce jeden min k el max el, drugi max p-k najmiejszych
from queue import PriorityQueue

def Merge_sort(T):
    n=len(T)
    if n > 1:
        pivot = n // 2
        L=T[:pivot]
        P=T[pivot:]
        Merge_sort(L)
        Merge_sort(P)
        m_i=0
        l_i=0
        p_i=0
        while l_i<len(L) and p_i<len(P):
            if L[l_i][0] <= P[p_i][0]:
                T[m_i]=L[l_i]
                l_i+=1
            else:
                T[m_i]=P[p_i]
                p_i+=1
            m_i+=1
        while l_i<len(L):
            T[m_i]=L[l_i]
            l_i+=1
            m_i+=1
        while p_i<len(P):
            T[m_i]=P[p_i]
            p_i+=1
            m_i+=1

def ksum(T, k ,p):
    n = len(T)
    kopiec_min = PriorityQueue()
    kopiec_max = PriorityQueue()
    new_T = T[0:p]
    is_in_min = [False for _ in range(n)]
    for i in range(p):
        new_T[i] = [new_T[i],i]
    Merge_sort(new_T)
    for i in range(p-k,p):
        kopiec_min.put(new_T[i])
        is_in_min[new_T[i][1]] = True
    for i in range(p-k):
        kopiec_max.put([-new_T[i][0],new_T[i][1]])
    last_del = -1
    indx = p
    suma = 0
    
    valz,indz = kopiec_min.get()
    suma+=valz
    last_del = indz
    kopiec_min.put([valz,indz])
    
    zdj = 0
    
    for i in range(n-p):
        
        if is_in_min[last_del] and last_del != -1:
            print("siusiak")
            is_in_min[last_del] = False
            kopiec_max.put([-T[indx],indx])
            val,ind = kopiec_max.get()
            if ind < i:
                while ind < i:
                    val,ind = kopiec_max.get()
            val = -val
            kopiec_min.put([val,indx])
            zdj+=1
        else:
            kopiec_max.put([-T[indx],indx])
        
        val,ind = kopiec_max.get()
        if ind < i:
            while ind < i:
                val,ind = kopiec_max.get()
        val = -val
        
        val2,ind2 = kopiec_min.get()
        print(val2,ind2,i)
        if ind2 < zdj:
            while ind2 <= i:
                val2,ind2 = kopiec_min.get()
                
        if val > val2:
            kopiec_max.put([-val2,ind2])
            kopiec_min.put([val,ind])
            val3,ind3 = kopiec_min.get()
            print([val3,ind3])
            suma+=val3
            kopiec_min.put([val3,ind3])
        else:
            suma+=val2
            print([val2,ind2])
            kopiec_min.put([val2,ind2])
            kopiec_max.put([-val2,ind2])
        print(suma)
        last_del = i
        if indx < len(T):
            indx+=1
            
    return suma
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=False )

T =  [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
k =  2
p =  4

print(ksum(T,k,p))
