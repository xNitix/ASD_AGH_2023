from zad1testy import runtests

def merge_sort(T):
    n = len(T)
    if n > 1:
        pivot = n // 2
        L = T[:pivot]
        P = T[pivot:]
        
        merge_sort(L)
        merge_sort(P)
        
        m_indx = 0
        l_indx = 0
        p_indx = 0
        
        while l_indx < len(L) and p_indx < len(P):
            if L[l_indx] <= P[p_indx]:
                T[m_indx] = L[l_indx]
                l_indx += 1
                m_indx += 1
            else:
                T[m_indx] = P[p_indx]
                p_indx += 1
                m_indx += 1
                
        while l_indx < len(L):
            T[m_indx] = L[l_indx]
            l_indx += 1
            m_indx += 1
            
        while p_indx < len(P):
            T[m_indx] = P[p_indx]
            p_indx += 1
            m_indx += 1
        
        
def chaos_index( T ):
    n = len(T)
    New_T = [[]for _ in range(n)]
    for i in range(n):
        New_T[i] = [T[i],i]
    merge_sort(New_T)
    k = 0
    for i in range(n):
        k = max(k,abs(New_T[i][1] - i))
    
    return k


runtests( chaos_index )
