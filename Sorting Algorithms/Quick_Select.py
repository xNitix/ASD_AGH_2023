# Quick_select - O(n) ? element tablicy ktory bedzie na katej pozycji po posortowaniu
# za pomoca funkcji particion z quick_sorta szukamy jaki wyrzuci nam indeks po 
# jako pierwszy posortowany element, jesli jest on rowny naszemu zadanemu to 
# zwracamy wartosc pod nim, jesli jest miejszy to dajemy do funkcji sort lewa storne
# tablicy jesli wiekszy to prawa bo wiadomo ze nasz indeks bedzie musial byc po
# ktorejs z nich

def Quick_select(T,q):
    def particion(T,p,k):
        x=T[k]
        i=p-1
        for j in range(p,k):
            if T[j] <= x:
                i+=1
                T[i],T[j]=T[j],T[i]
        T[i+1],T[k]=T[k],T[i+1]
        return i+1

    def select(T,q,p,k):
        x = particion(T,p,k)
        if x == q:
            return T[q]
        if x > q:
            return select(T,q,p,x-1)
        else:
            return select(T,q,x+1,k)
        
        
    def select_it(T,q,p,k):
        x=particion(T, p, k)
        while x!=q:
            if x > q:
                x = particion(T, p, x-1)
            else:
                x = particion(T, x+1, k)
        return T[x]


    return select_it(T, q, 0, len(T)-1)