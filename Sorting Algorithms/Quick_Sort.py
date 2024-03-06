# Quicsort - O(nlogn) | pesymistyczna : O(n^2) | stabilność : NIE
# particion wybiera pivot na ostatni element i sprawdza j ktore wartosci sa mniejsze lub
# rowne pivotowi, wtedy je swapuje miejscem z i ktore trzyma indeks ostatniej liczby
# ktora jest mniejsza/rowna od pivota, na koncu swapuje pivot z pierwszym elementem
# przed i czyli pierwszym wiekszym od niego i zwraca miejsce na ktorym jest juz 
# uporzadkowany element. sort bierze indeks tego piwota i rodziela rekurencyjnie tablice 
# na lewo i prawo od niego by je dalej posortowac uzywajac funkcji particion 
def Quick_sort(T):
    def particion(T,p,k):
        x = T[k]
        i=p-1
        for j in range(p,k):
            if T[j] <= x:
                i+=1
                T[i],T[j]=T[j],T[i]
        T[i+1],T[k]=T[k],T[i+1]
        return i+1
    def sort(T,p,k):
        if p < k:
            pivot = particion(T, p, k)
            sort(T, p, pivot-1)
            sort(T, pivot+1, k)
    sort(T, 0, len(T)-1)