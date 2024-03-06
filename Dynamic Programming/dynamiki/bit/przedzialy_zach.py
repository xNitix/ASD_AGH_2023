def przedzial(T,k):
    n = len(T)
    inf = float("inf")
    T.sort(key=lambda x: x[1])
    res = [None]
    min = inf
    
    for i in range(n):
        ile = 1
        tab=[T[i]]
        koniec = T[i][1]
        poczatek = T[i][0]
        for j in range(i+1,n):
            if ile == k:
                break
            if T[i][1] <= T[j][0] and koniec <= T[j][0]:
                ile += 1
                koniec = T[j][1]
                tab.append(T[j])
        if koniec - poczatek < min and ile == k:
            res = tab
            min = koniec - poczatek
    
    return res
    
T = [[6,10],[1,2],[2,4],[3,4],[4,5],[4,5],[3,6],[6,7],[7,8]]
k = 4

print(przedzial(T,k))
                