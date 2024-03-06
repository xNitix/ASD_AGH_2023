# n^2 * k zakladam ze biore pierwszy element i szukam najwiekszego przeciecia, potem zakladam ze biore pierwszy itd ..
from zad3testy import runtests

# 1 - rozwiazanie z bitu, memoryzacja macierz n*k
# def intersect(A,B):
#   inf = float("inf")
#   s_A = A[0]
#   s_B = B[0]
#   e_A = A[1]
#   e_B = B[1]
  
#   if s_A >= s_B and e_A <= e_B:
#     return A
#   if s_A < s_B and e_A > e_B:
#     return B
  
#   if e_A < s_B or e_B < s_A:
#     return [0,0]
  
#   if s_A <= s_B and e_A <= e_B and s_B < e_A :
#     return [s_B,e_A] 
#   if s_A <= s_B and e_A <= e_B and s_B <= e_A :
#     return [s_B,s_B]
  
#   if s_B <= s_A and e_B <= e_A and s_A < e_B :
#     return [s_A,e_B]
#   if s_B <= s_A and e_B <= e_A and s_A <= e_B :
#     return [s_A,s_A]
  
#   if s_A == s_B and e_A < e_B:
#     return[s_A,e_A]
#   if s_A == s_B and e_A > e_B:
#     return[s_A,e_B]
  
  
  

# def kintersect( A, k ):
#   n = len(A)
#   inf = float("inf")
#   compar = [[[0,0]for _ in range(k+1)]for _ in range(n+1)]
#   compar_indx = [[0 for _ in range(k+1)]for _ in range(n+1)]
#   for i in range(n):
#     compar[i][0] = A[i]
#     compar_indx[i][0] = i
#   A.append([-inf,inf])
  
#   def f(compar,A,i,k):
#     if k == 0:
#       return compar[i][k]
    
#     if i - k < 0:
#       return [0,0]
    
#     if compar[i][k] != [0,0]:
#       return compar[i][k]
    
#     max_len = 0
#     com = [0,0]
#     ind = 0
#     for j in range(i):
#       curr = intersect(f(compar,A,j,k-1),A[i])
#       if curr != [0,0]:
#         curr_len = curr[1] - curr[0]
#         if curr_len > max_len:
#           max_len = curr_len
#           com = curr
#           ind = j
          
#     compar[i][k] = com
#     compar_indx[i][k] = ind
#     return com
  
#   f(compar,A,n,k)
  
#   res = [n]
#   for i in range(k,-1,-1):
#       x = (compar_indx[res[len(res)-1]][i])
#       if res[len(res)-1] != x:
#         res.append(x)
    
#   return res[1:]

# rozwiazanie basi, skoro są 3 takie odcinki (k) to cale te przedzialy beda musialy w pewnym ulozeniu sie opatulac, wiec pierwszym forem szukam przedzialu ktory bedzie sie najbardziej 
# zawierac w potencjalnej grupie, a potem szukam tych co go beda otaczac, ich kolejnosc jest niewazne bo i tak najmiejszym przedzialem bedzie ten srodkowym, wazne tylko zeby pierwsza 
# wspolrzedna byla mniejsza lub rowna mojemu pierwszemu przedzialowi, zeby mogly go w calosci otoczyc. Sortuje po najdalyszch koncach i biore te ktore zaczynaja sie wczesniej lub tam gdzie
# ja po to zeby na poczatku przejrzec wszytskie mozliwosci przedzilow wiekszych ode mnie. Powstana przedzialy ktore na siebie nie nachodza, ale wtedy curr bedzie ujemny, wiec
# ten wiekszy i tak go potem zmieni, a nie moze byc tak ze np w trakcie mi wyjdzie ujemny a potem sie zmieni na dodatni bo sa posortowane po koncach wiec jak juz sie trafia takie co 
# sie nie nacinaja to kazde kolejne takie bedzie- n^2 bez stalem k

def kintersect(A, k):
    n = len(A)
    inf = float('inf')
    for i in range(n):
        A[i] = [A[i][0], A[i][1], i]

    A.sort(key=lambda x: x[1], reverse=True)
    # zbiór indeksów przedziałów o największym przecięciu
    best = []
    # rozmiar najlepszego przecięcia
    diff = -inf

    # wybieram pierwszy przedział
    for first in range(n):
        s, e, idx = A[first]
        curr = [s, e]
        cnt = 1
        res = [idx]

        # szukam kolejnych k-1 przedziałów
        for new in range(n):

            # start,koniec przedziału,idx w wejsciowej tab
            newS, newE, newIdx = A[new]
            if newIdx not in res and cnt < k:
                if newS <= s:
                    cnt += 1
                    res.append(newIdx)
                    curr = [max(curr[0], newS), min(curr[1], newE)]
                    # nie musi byc, ale tu wlasnie jak trafi sie jeden pusty to wiadomo ze wszytskie inne tez puste
                    if curr[0] > curr[1]:
                        break

            # jak znajde k przedziałów
            if cnt == k:
                # sprawdzam czy ich przecięcie jest większe od ostatnio zapisanego
                if curr[1] - curr[0] > diff:
                    diff = curr[1] - curr[0]
                    best = res[:]
                    break
    return best


runtests( kintersect )

# A = [(0,4),(9,10),(3,7), (2,8)]
# k=3

# A2 = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
# k2 = 3

# print(kintersect(A2,k2))

