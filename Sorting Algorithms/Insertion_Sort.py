# Insertion sort O(n^2)
#Algorytm symulujacy sortowanie jak tali kart w rece, lecimy pierwsszym skaznikiem
#po kazdym elemencie w srodku mam y druga petle ktora staruje od tego samego miejsca
#i jesli element jest mniejszy niz wczenisiejszy to zamianiamy wszytskie elemnty
#az nie trafi on na dobre miejsce
def insertion_sort( T ):
    n=len(T)
    for i in range(1,n):
        j=i
        while j > 0 and T[j] < T[j-1]:
            T[j],T[j-1]=T[j-1],T[j]
            j-=1
