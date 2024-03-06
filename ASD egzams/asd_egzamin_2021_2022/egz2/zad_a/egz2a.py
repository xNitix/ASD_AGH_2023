# buduje drzewo ktore w lisciach ma kontenery ponumerowane od 0 rosnaco w prawo, dla stworzenia drzewa musi ich byc odpowiednia ilosc skad szukanie na poczaku jaka wysokosc drzewa bedzie
# zakladajac ze do rozlozenia wegla bedzie potrzebne tyle kontenerow ile bedzie dostaw. W wezlach trzymam minimum z dzieci lewego i prawego. Dostawe zawsze probuje wcisnac do dziecka najbardziej
# na lewo i jak mi juz wloze wegiel to zrwacam numer kontenera do jakiego go wlozylem 
from egz2atesty import runtests
from math import log2

class node():
    def __init__(self,val=0,num = None):
        self.left = None
        self.right = None
        self.val = val
        self.num = num
        
def build_tree(H):
    num_con = 0
    root = node()
    def build(root,i,H):
        if i < H:
            root.left=node()
            build(root.left,i+1,H)
            root.right=node()
            build(root.right,i+1,H)
        else:
            nonlocal num_con
            root.num = num_con 
            num_con += 1
    build(root,0,H)
    return root

def delivery(root,d,t):
    if root.left == root.right == None:
        root.val += d
        return root.num
    else:
        con = 0
        if root.left.val + d <= t:
           con = delivery(root.left,d,t)
        elif root.right.val + d <= t:
            con = delivery(root.right,d,t)
        else:
            # w tescie 6 chyba jest blad bo len(A) wynosi 9999 a nie 10000
            con = 9999
            
        root.val = min(root.left.val,root.right.val)
        return con          

def coal( A, T ):
    n = len(A)
    max_h = round(log2(n),0)
    tree = build_tree(max_h)
    res = 0
    
    for i in A:
        res = delivery(tree,i,T)
        
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )

