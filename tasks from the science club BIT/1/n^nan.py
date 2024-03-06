from math import log10
def count_sort(T,base,div):
    n=len(T)
    C=[0]*(base+1)
    B=[0]*n
    for i in range(n):
        C[(T[i]//div)%base]+=1
    for i in range(1,base+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[(T[i]//div)%base]-1]=T[i]
        C[(T[i]//div)%base]-=1
    for i in range(n):
        T[i]=B[i]

def radix_sort(T):
    n = len(T)
    max_val = max(T)
    divider = 1
    while max_val >= divider:
        count_sort(T,n,divider)
        divider = divider * n
    return T


T = [7,12,2,4]

print(radix_sort(T))
    
    
    