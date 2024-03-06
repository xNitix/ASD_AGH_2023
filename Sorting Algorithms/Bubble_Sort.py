# Bubble sort - 0(n^2)
# przechodzimy po tablicy porownujac obecny element z nastepnym, jesli jest wiekszy to go swapujemy(wyplywa do gory tablicyj jak bombelek)
# czynnosc powtzracmy n razy ( n - dlugosc tablicy)
def Bubble_Sort(T):
    n=len(T)
    for i in range(n):
        for j in range(n-1):
            if T[j] > T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]