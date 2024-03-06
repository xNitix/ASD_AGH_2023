# Selection sort O(n^2)
# ustawiamy minimum na pierwszy element i przechodzimy po tablicy swapujac za kazdym razem gdy znajdziemy mnieszy elemet, nastepnie
# ustawiamy najmiejszy element na drugi itd.

def Selection_sort(T):
    n=len(T)
    for i in range(n):
        for j in range(i,n):
            if T[j] < T[i]:
                T[i],T[j]=T[j],T[i]