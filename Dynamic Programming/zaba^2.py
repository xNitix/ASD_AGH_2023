# nie da sie zrobic zachlan bo jesli skaczemy o dwa to koszt jest -4 okazuje sie ze musimy i tak zebrac wczesniejsze i 
# wtedy moglismy skoczyc dwa razy po jeden i by bylo -2 zamiast -4

def zaba_kw(T):
    inf = float("inf")
    n = len(T)
    suma = 0
    for i in range(n):
        suma += T[i]
    dp = [[inf for _ in range(suma+1)]for _ in range(n)]
    dp[0][T[0]] = 0
    
    for i in range(1,n):
        for j in range(i):
            for energy in range((i-j)**2,suma+1): # moze byc (suma+1) ale wiecej niepotrzebnych operacji
                if dp[j][energy] != inf:
                    # ten if niepotrzebny jesli energy od (i-1)**2
                    if energy - (i-j)**2 >= 0:
                        dp[i][energy - (i-j)**2 + T[i]] = min(dp[i][energy - (i-j)**2 + T[i]],dp[j][energy] + 1)
    
    print(*dp,sep='\n')
    return min(dp[n-1])
A=[2,4,1,2,0,0,1,1]
print(zaba_kw(A))