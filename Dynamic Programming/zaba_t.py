def frog(T):
    n = len(T)
    snack = []
    for i in range(n-1,-1,-1):
        if T[i] != 0:
            snack.append([T[i],i])
    bak = snack[len(snack)-1][0]
    snack.remove(snack[len(snack)-1])
    snack.sort(key = lambda x : x[0],reverse = True)
    pole = 0
    snack_cunter = 0
    i = 0
    while True:
        # warunki koncowe
        if (n-1 - pole)**2 <= bak and pole != n-1:
            snack_cunter+=1
            return snack_cunter
        if (n-1 - pole)**2 <= bak:
            return snack_cunter
        # warunek braku mozliwosci dojscia
        if len(snack) == 0 or i >= len(snack):
            return None
        
        energy,stop = snack[i]
        # przekaska jest za nami
        if stop <= pole:
            bak += energy
            snack.remove([energy,stop])
            snack_cunter+=1
        # porzekąska przed nami, ale damy rade doskoczyc
        elif bak - (stop - pole)**2 >= 0:
            bak = bak - (stop - pole)**2 + energy
            pole = stop
            snack_cunter+=1
            snack.remove([energy,stop])
        # przekąska przed nami i nie damy rady
        else:
            i+=1
    
            
A=[2,4,1,2,0,0,1,1]

print(frog(A))
        
        
    