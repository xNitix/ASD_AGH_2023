# We are given three strings A, B and C. A and B are of the same length. The following properties apply:
#   1) Letters at the sane index in strings A and B are equivalent
#   2) If letter a is equivalent with letter b, then letter b is equivalent with letter a
#   3) If letter a is equivalent with letter b and letter b is equivalent with letter c, then letter
#      a is equivalent to letter c
#   4) Each letter is equivalent to itself
# In string C we can replace any letter with a letter equivalent to it. What is the smallest
# lexicographically string that we can create in this way?

class node:
    def __init__(self,L):
        self.val = L
        self.parent = self
        self.rank = 0
        
def findset(l):
    if l != l.parent:
        l.parent = findset(l.parent)
    return l.parent

def union(l1,l2):
    l1 = findset(l1)
    l2 = findset(l2)
    if l1.rank > l2.rank:
        l2.parent = l1
    else:
        l1.parent = l2
        if l1.rank == l2.rank:
            l2.rank += 1
            
def main(A,B,C):
    n = len(A)
    nodes = []
    letters = []
    for i in range(n):
        if A[i] not in letters and B[i] not in letters:
            L1 = node(A[i])
            L2 = node(B[i])
            nodes.append(L1)
            nodes.append(L2)
            letters.append(A[i])
            letters.append(B[i])
        elif A[i] not in letters and B[i] in letters:
            L1 = node(A[i])
            nodes.append(L1)
            letters.append(A[i])
            indx_B = letters.index(B[i])
            L2 = nodes[indx_B]
        elif A[i] in letters and B[i] not in letters:
            L2 = node(B[i])
            nodes.append(L2)
            letters.append(B[i])
            indx_A = letters.index(A[i])
            L1 = nodes[indx_A]
        elif A[i] in letters and B[i] in letters:
            indx_A = letters.index(A[i])
            L1 = nodes[indx_A]  
            indx_B = letters.index(B[i])
            L2 = nodes[indx_B] 
        union(L1,L2)
    
    C_list = list(C)
    n_c = len(C_list)
    for i in range(n_c):
        if C[i] in letters:
            indx_c = letters.index(C[i])
            c_node = letters[indx_c]
            while c_node != c_node.parent:
                c_node = c_node.parent
            C_list[i] = c_node.val
    return C_list

    