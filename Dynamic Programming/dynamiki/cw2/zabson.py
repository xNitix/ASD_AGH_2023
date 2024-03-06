def zabson(T):
    n = len(T)
    inf = float("inf")
    
    snack_sum=0
    for i in range(n):
        snack_sum+=T[i]
    
    energy = [[inf for _ in range(snack_sum+1)]for _ in range(n)]
    energy[0][T[0]] = 0

    
    for end in range(1,n):
        for start in range(end):
            for start_energy in range((end-start)**2,snack_sum+1):
                end_energy = start_energy - (end - start)**2 + T[end]
                
                if end_energy >= snack_sum:
                    end_energy  = snack_sum - 1

                if energy[end][end_energy] > energy[start][start_energy] + 1:
                    energy[end][end_energy] = energy[start][start_energy] + 1

    
    return min(energy[n-1])
    
T=[2,4,1,2,0,0,1,1]

print(zabson(T))
