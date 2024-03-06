from zad3testy import runtests
import math

def bombel_sort(bucket):
    n = len(bucket)
    for i in range(n):
        for j in range(n-1):
            if bucket[j] > bucket[j+1]:
                bucket[j],bucket[j+1] = bucket[j+1],bucket[i]
    
def fast_sort(tab, a):
    n = len(tab)
    Buckets = [[]for _ in range(n)]
    for i in range(n):
        Buckets[int(n*(math.log(tab[i],a)))].append(tab[i])
    for i in range(n):
        bombel_sort(Buckets[i])
    tab_i=0
    for i in range(n):
        for j in range(len(Buckets[i])):
            tab[tab_i] = Buckets[i][j]
            tab_i += 1
    return tab



runtests( fast_sort )
