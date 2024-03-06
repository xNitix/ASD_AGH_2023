def particion(T,p,k):
    x = T[k]
    i = p-1
    for j in range(p,k):
        if T[j] <= x:
            i+=1
            T[i],T[j] = T[j],T[i]
    i+=1
    T[i],T[k] = T[k],T[i]
    return i

def seleciotn(T,p,k,i):
    x = particion(T,p,k)
    if x == i:
        return True
    elif i > x:
        seleciotn(T,x+1,k,i)
    else:
        seleciotn(T,p,x-1,i)
        
def section(T,p,q):
    seleciotn(T,0,len(T)-1,p)
    seleciotn(T,p+1,len(T)-1,q)
    return T[p:q+1]
    
T = [190,192,189,168,172,168,190,200,169,166,168,195]
print(section(T,6,9))
T.sort()
print(T)