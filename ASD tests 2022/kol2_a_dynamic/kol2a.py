from kol2atesty import runtests

def drivers( P, B ):
    p = True
    c = False
    inf = float('inf')
    # dp[i][driver] - liczba punktow kontrolnych
    # jaka przejedzie marian, jesli w i prowadzi driver
    n = len(P)
    P1 = [(P[i][0], P[i][1], i) for i in range(n)]
    P1.append((B, p, n))
    P1.sort(key=lambda x: x[0])
    n += 1
    jacek = 0
    marian = 1

    dp = [[inf, inf] for _ in range(n)]
    parent = [[None, None] for _ in range(n)]
    
    i = 0
    no_switch = 0 # number of switches
    start_mar = -1 # first place where marian can take over
    while i < n and no_switch < 3:
        if P1[i][1] == p:
            dp[i][jacek] = 0
            if no_switch == 1:
                start_mar = i
            no_switch += 1
        i += 1
    
    if start_mar == -1:
        return []

    for i in range(start_mar, n):
        if P1[i][1] == p:
            if dp[i][jacek] == inf:
                j = i - 1
                no_switch = 0
                while j >= 0 and no_switch < 3:
                    if P1[j][1] == p:
                        if dp[i][jacek] > dp[j][marian]:
                            dp[i][jacek] = dp[j][marian]
                            parent[i][jacek] = (j, marian, no_switch)
                        no_switch += 1
                    j -= 1
            
            j = i - 1
            no_switch = 0
            checkpoints = 0
            while j >= 0 and no_switch < 3:
                if P1[j][1] == p:
                    if dp[i][marian] > dp[j][jacek] + checkpoints:
                        dp[i][marian] = dp[j][jacek] + checkpoints
                        parent[i][marian] = (j, jacek, no_switch)
                    no_switch += 1
                else:
                    checkpoints += 1
                j -= 1
    print(dp,sep='\n')
    #i = n - 1
    #while P1[i][1] == c:
    #    i -= 1

    driver = -1
    if dp[i][jacek] < dp[i][marian]:
        driver = jacek
    else:
        driver = marian
    
    #print(dp[i][jacek], dp[i][marian])
        
    sol = []
    #if parent[i][driver][2] == 2:
    #    sol.append(P1[i][2])
    
    while parent[i][driver] != None:
        switch_id, new_driver, _ = parent[i][driver]
        sol.append(P1[switch_id][2])
        i = switch_id
        driver = new_driver

    return sol

    
        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )