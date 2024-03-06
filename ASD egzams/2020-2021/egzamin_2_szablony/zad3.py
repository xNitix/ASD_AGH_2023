from zad3testy import runtests
from math import log2
from math import ceil

class node():
    def __init__(self,colors=[0,0,0],span = None):
        self.left = None
        self.right = None
        self.colors = colors #N|Z|C
        self.span = span
        self.all = 0
        
def build_tree(H):
    num_con = 0
    root = node()
    def build(root,i,H):
        if i < H:
            root.left=node()
            build(root.left,i+1,H)
            root.right=node()
            build(root.right,i+1,H)
            root.span = [root.left.span[0],root.right.span[1]]
            root.colors = [root.left.colors[0] + root.right.colors[0],root.left.colors[1] + root.right.colors[1],root.left.colors[2] + root.right.colors[2]]
        else:
            nonlocal num_con
            root.span = [num_con,num_con]
            root.colors = [0,1,0]
            num_con+=1
            
    build(root,0,H)
    return root

def delivery(root,span):
    if root.left == root.right == None:
        root.colors[0],root.colors[1],root.colors[2] = root.colors[2], root.colors[0], root.colors[1]
        return
    elif root.span == span:
        root.colors[0],root.colors[1],root.colors[2] = root.colors[2], root.colors[0], root.colors[1]
        root.all += 1
        return
    elif root.left.span[0] <= span[0] and root.left.span[1] >= span[1]:
        delivery(root.left,span)
    elif root.right.span[0] <= span[0] and root.right.span[1] >= span[1]:
        delivery(root.right,span)
    else:
        delivery(root.left,[span[0],root.left.span[1]])
        delivery(root.right,[root.right.span[0],span[1]])
    
    root.colors = [root.left.colors[(0+3-(root.all)%3)%3] + root.right.colors[(0+3-(root.all)%3)%3],root.left.colors[(1+3-(root.all)%3)%3] + root.right.colors[(1+3-(root.all)%3)%3],root.left.colors[(2+3-(root.all)%3)%3] + root.right.colors[(2+3-(root.all)%3)%3]]

def lamps(n, A):
    max_h = ceil(log2(n))
    tree = build_tree(max_h)
    
    max_blue = 0
    for i in A:
        delivery(tree,i)
        max_blue = max(max_blue,tree.colors[0])
        
    return max_blue
    
runtests( lamps )


