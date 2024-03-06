# Radix sort - O(d(n+k)) | pesymistyczna : O(n+k) | stabilność : TAK
# d = (logp(n)+1) gdzie p to podstawa naszego systemu (np 10), wiec jak jest zadanie z
# liczbamy z zakresu od 0 do n^2-1 to mozemy przejsc na system dzisietny i z log sie 
# zrobi stala dzieki czemu wyjdzie nam sortowanie liniowe
# przevhodze albo po koncach liczb albo po ostatnich loterach i soertuje je po nich
# dzieki zachowaniu stabilosci count_sorta w kolejneych zamianach nie zamienia
# sie kolejnosci tych samych fragmentow 

from Count_Sort import Count_sort_string, Count_sort_int
def radix_sort_string(T):
    n=len(T[0])
    for i in range(n-1,-1,-1):
        Count_sort_string(T, i)

from math import log10
def radix_sort_int(T):
    # jako n trzeba podac jakiego rozamiaru jest najwieksza liczba
    n=int(log10(T[0]))+1
    for i in range(n):
        Count_sort_int(T,i)