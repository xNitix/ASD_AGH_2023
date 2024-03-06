# *8 Cykl hamiltona - odwiedza kazdy wierzcholek dokladnie raz - Brut Force sprawdza O(V!) mozliwosci Nie da sie lepiej bo rozpoznawanie
# czy graf ma cykl hamiltiona to problem np trudny ( jest to tez algorytm znajdywania najdluzszej sciezki w grafie, wystarczy usunac 1 krawdz)

# def permutacje(lista,indx):
#     if indx < len(lista):
#         for i in range(indx,len(lista)):
#             lista[i],lista[indx]=lista[indx],lista[i]
#             permutacje(lista,indx+1)
#             lista[i],lista[indx]=lista[indx],lista[i]
#     else:
#         print(lista)

def hamilton(G):
    n = len(G)
    flaga=0
    res=[]
    lista=[ i for i in range(n)]
    def permutacje(G,lista,indx):
        if indx < len(lista):
            for i in range(indx,len(lista)):
                lista[i],lista[indx]=lista[indx],lista[i]
                permutacje(G,lista,indx+1)
                lista[i],lista[indx]=lista[indx],lista[i]
        else:
            nonlocal res
            flaga = 0
            for i in range(len(lista)-1):
                if G[i][i+1] == G[i+1][i] == 0:
                    flaga = 1
                    break
            if flaga == 0:
                res=lista
        return False
    permutacje(G, lista, 0)
    return res

