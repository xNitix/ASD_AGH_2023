# Count sort - O(n+k) | pesymistyczna : O(n+k) | stabilność : TAK
# oplaca sie go uzywac tylko gdy nasze dane do posortowania są z jakiegos danego niewielkiego zakresu, tworzymy wtedy tablice gdzie
# umieszczamy na odpowiednich indeksach ile razy dana wafrtosc wystepuje w naszej tablicy (gdy elementy sa od 0 do k to indeksujemy
# normalnie, w przeciwnym wypadku mozemy za kazdym razem odejmowac stala poczatku, wtedy sie przeskaluje) nastepnie w tablicy sumujemy
# ile dla danego indeksu jest elementow mniejszych badz rownych jemu, a nastepnie idac od konca orginalnaej tablicy sprawdzamy ile
# jest dla danej liczy mniejszych badz rownych jej i ustawiamy w tablicy wnikowej pod tym indeksem -1, ostatecznie przepisujemy wynikowa
# tablice do orginalnej
def Count_sort(T,p,k):
    n=len(T)
    C=[0]*(k-p+1)
    B=[0]*n
    for i in range(n):
        C[T[i]-p]+=1
    for i in range(1,k-p+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[T[i]-p]-1]=T[i]
        C[T[i]-p]-=1
    for i in range(n):
        T[i]=B[i]

def Count_sort_string(T,indx):
    C=[0]*26
    B=[0]*len(T)
    for i in range(len(T)):
        C[ord(T[i][indx])-97]+=1
    for i in range(1,26):
        C[i]+=C[i-1]
    for i in range(len(T)-1,-1,-1):
        B[C[ord(T[i][indx])-97]-1]=T[i]
        C[ord(T[i][indx])-97]-=1
    for i in range(len(T)):
        T[i]=B[i]

def Count_sort_int(T,pow,base):
    n=len(T)
    C=[0]*base+1
    B=[0]*n
    for i in range(n):
        C[(T[i]//base**pow)%base]+=1
    for i in range(1,base+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[(T[i]//base**pow)%base]-1]=T[i]
        C[(T[i]//base**pow)%base]-=1
    for i in range(n):
        T[i]=B[i]