from egz1atesty import runtests

def snow( S ):
    def merge_sort(S):
        if len(S) > 1:
            pivot = len(S)//2
            L = S[:pivot]
            P = S[pivot:]
            
            merge_sort(L)
            merge_sort(P)
            
            indx_l=0
            indx_p=0
            indx_g=0
            
            while indx_l < len(L) and indx_p < len(P) and indx_g < len(S):
                if L[indx_l] >= P[indx_p]:
                    S[indx_g] = L[indx_l]
                    indx_l+=1
                    indx_g+=1
                else:
                    S[indx_g] = P[indx_p]
                    indx_p+=1
                    indx_g+=1
            
            while indx_l < len(L):
                S[indx_g] = L[indx_l]
                indx_l+=1
                indx_g+=1
                
            while indx_p < len(P):
                S[indx_g] = P[indx_p]
                indx_p+=1
                indx_g+=1
            
    merge_sort(S)
    n = len(S)            
    i = 0
    suma = 0
    while S[i] - i > 0 and i < n:
        suma += S[i] - i
        i+=1
        
    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
