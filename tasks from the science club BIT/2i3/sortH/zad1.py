from zad1testy import Node, runtests

def left(i): 
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i-2) // 2

def heapify(A,i,n):
    l = left(i)
    r = right(i)
    min_indx = i
    if l < n and A[l].val < A[min_indx].val:
        min_indx = l
    if r < n and A[r].val < A[min_indx].val:
        min_indx = r
    
    if min_indx != i:
        A[i],A[min_indx] = A[min_indx],A[i]
        heapify(A,min_indx,n)
        
def buildheap(A):
    n = len(A)
    for i in range(parent(n),-1,-1):
        heapify(A,i,n)

class Node:
    def __init__(self,val):
        self.val = val # liczba
        self.next = None # odsylacz

def SortH(p,k):
    if k == 0:
        return p
    p1 = p
    nodes = []
    while p1 != None:
        nodes.append(p1)
        p1=p1.next
        
    if len(nodes) <= k:
        k = len(nodes) - 1
        
    kopiec_min = []
    i = 0
    
    while i <= k:
        kopiec_min.append(nodes[i])
        i+=1
        
    buildheap(kopiec_min)
    
    inf = float("inf")
    kopiec = kopiec_min[0]
    res = kopiec

    while kopiec_min[0].val != inf:
        if i < len(nodes):
            kopiec_min[0] = nodes[i]
            heapify(kopiec_min,0,k+1)
            kopiec.next = kopiec_min[0]
            kopiec = kopiec.next
            i+=1
        else:
            kopiec_min[0] = Node(inf)
            heapify(kopiec_min,0,k+1)
            if kopiec_min[0].val != inf:
                kopiec.next = kopiec_min[0]
                kopiec = kopiec.next
                
    kopiec.next = None
                
    return res
    
runtests( SortH ) 

T = [545, 135, 283, 295, 768, 36, 1107, 334]
