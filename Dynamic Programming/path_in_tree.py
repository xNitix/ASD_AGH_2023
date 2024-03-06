class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def best_tree(v):
    if v == None:
        return [0,0]
    
    best_l,L = best_tree(v.left)
    best_r,R = best_tree(v.right)
    
    # zaczyna sie 
    best_in = max(0,v.val,v.val+L,v.val+R)
    
    # przechodzi przez
    best_all = max(best_l,best_r,best_in,v.val+L+R)
    
    return [best_all,best_in]

def main(T):
    return max(best_tree(T))


A = Node(-5)
B = Node(1)
C = Node(50)
D = Node(20)
E = Node(5)
E.left = A
E.right = B
F = Node(-10)
F.left = C
F.right = D
G = Node(10)
G.left = E
G.right = F

print(main(G))

    