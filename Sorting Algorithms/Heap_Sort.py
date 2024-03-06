# Heap sort - O(nlogn) | pesymisztyczna : O(nlogn) | stabilność : NIE
# Z tablicy tworzymy drzewo binarne gdzie kazdy rodzic jest wiekszy od swoich dzieci
# robi to funkcja build heap, funkcja heap sort bierze nawjieszka wartosc ktora znajduje
# sie w korzeniu daje ja na poczatek tablicy a nastepnie uruchania na drzewie funkcje
# heapyfiy ktora naprawia kopiec tak by heapsort mogl pobrac kolejny najwiekszy element
def Heap_sort(T):
    def parent(i):
        return (i-2)//2
    def left(i):
        return 2*i+1
    def rigth(i):
        return 2*i+2
    def heapify (T,i,n):
        l=left(i)
        r=rigth(i)
        max_indx=i
        if l < n and T[l] > T[max_indx]:
            max_indx=l
        if r < n and T[r] > T[max_indx]:
            max_indx=r
        if max_indx != i:
            T[max_indx],T[i]=T[i],T[max_indx]
            heapify(T, max_indx, n)
    def build_heap(T):
        n=len(T)
        # parent(n-1) ?
        for i in range(parent(n),-1,-1):
            heapify(T, i, n)
    def heapsort(T):
        n = len(T)
        build_heap(T)
        for i in range(n-1,0,-1):
            T[0],T[i]=T[i],T[0]
            heapify(T, 0, i)
    heapsort(T)