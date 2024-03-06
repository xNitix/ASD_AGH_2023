# Merge sort - O(nlogn) | pesymistyczna : O(nlogn) | stabilość : TAK
# dostajemy tablice i dzielimy ją na dwie czesci (arr[start:stop] # items start through stop-1)
# od poczatku do pivota i od pivota wlacznie do konca, rekurencyjnie sortujemy te dwie
# tablice a nastepnie scalamy w jedna 
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
            if L[l_i] <= P[p_i]:
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