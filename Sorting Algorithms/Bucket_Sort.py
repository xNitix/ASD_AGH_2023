# Bucket sort - O(n) | pesymistyczna : O(n^2) | stabilność : TAK
# mamy tablice A gdzie jej elementy spelniaja warunek 0 <= A[i] < 1, oraz są 
# wygenerowane zgodnie z rozkladem jednostajnym, tworzymy n kubełkow, nastepnie
# przegladamy tablice A i aktualna liczbe A[i] umieszczamy w kubelku [n*A[i]] 
# potem kazdy kubelek segregujemy wewenetrznie i przepisujemy kolejnoscia do A   
def insertion_sort( T ):
    n=len(T)
    for i in range(1,n):
        if T[i] == None:
            break
        j=i
        while j > 0 and T[j] < T[j-1]:
            T[j],T[j-1]=T[j-1],T[j]
            j-=1
            
def bucket_sort(T):
    n=len(T)
    Buckets=[]
    for i in range(n):
        Buckets.append([])
    for i in range(n):
        Buckets[int(T[i]*n)].append(T[i])
    for i in range(n):
        insertion_sort(Buckets[i])
    res_indx=0
    for i in range(n):
        for j in range(len(Buckets[i])):
            T[res_indx]=Buckets[i][j]
            res_indx+=1
        
    
from math import log10
def bucket_sort_int(T):
    n=len(T)
    max_v=max(T)
    min_v=min(T)
    buckets= [[] for _ in range(n)]
    for i in range(n):
        buckets[int((T[i]-min_v)/10**int(log10(max_v)+1))].append(T[i])
    for i in range(n):
        insertion_sort(buckets[i])
    k=0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[k]=buckets[i][j]
            k+=1
