def roznica( S ):
    n = len(S)
    inf = float("inf")
    ile = [[-inf for _ in range(n)]for _ in range(n)]
    for i in range(n):
        if S[i] == "0":
            ile[i][i] = 1
        else:
            ile[i][i] = -1  
    
    for a in range(n):
        for b in range(a+1,n):
            if S[b] == "0":
                ile[a][b] = ile[a][b-1] + 1
            else:
                ile[a][b] = ile[a][b-1] - 1
                
    maxi = -inf
    
    for i in range(n):
        for j in range(n):
            maxi = max(maxi,ile[i][j])
            
    return maxi

string = "11000010001"

print(roznica(string))