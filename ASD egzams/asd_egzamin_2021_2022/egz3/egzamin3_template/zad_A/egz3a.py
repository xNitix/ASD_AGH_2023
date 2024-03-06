#Tworze drzewo z podanych przedzialow i porzy dodawanaiu sniegu sa trzy opcje, albo moj przedzial pasuje idealanie do 
#przedzialu za ktore odpowiada dany wezel, albo miesci sie w calopsci w ktoryms x przedzialow dzieci, lub 3 trzeba
#podzielic przedzial na pol i tak az nie dojdziemy do lisci, w gore jako sume w pojedynczym wezle uznalejy to ile 
#przedzialow do niego idealnie pasowalo + max z sumy jego dzieci 
from egz3atesty import runtests
from math import log2
from math import ceil

class node:
    def __init__(self,span = None,val = 0):
        self.left = None
        self.right = None
        self.span = span
        self.val = val
        self.sum = 0
        
def build_tree(H,T,uni):
    km_count = 0
    
    def build(root,i,H):
        if i >= H:
            nonlocal km_count
            if len(uni) > km_count:
                root.span = [uni[km_count],uni[km_count]]
                km_count += 1
                return [uni[km_count - 1]]
            else:
                root.span = [uni[len(uni)-1]+km_count,uni[len(uni)-1]+km_count]
                km_count += 1
                return [uni[len(uni)-1]+km_count-1]
        else:
            root.left = node()
            root.right = node()
            L = build(root.left,i+1,H)
            R = build(root.right,i+1,H)
            if len(L) == len(R) == 1:
                root.span=[L[0],R[0]]
            else:
                root.span=[L[0],R[1]]
            return root.span
        
    root = node([0,T])
    build(root,0,H)
    return root

def snow_delivery(root,segment):
    if root.left == root.right == None:
        root.val += 1
        root.sum += 1
        #print(root.span,root.sum,segment)
        return
    elif root.span == segment:
        root.val += 1
        root.sum += 1
        #print(root.span,root.sum,segment)
        return
    elif root.left.span[0] <= segment[0] and root.left.span[1] >= segment[1]:
        snow_delivery(root.left,segment)
    elif root.right.span[0] <= segment[0] and root.right.span[1] >= segment[1]:
        snow_delivery(root.right,segment)
    else:
        snow_delivery(root.left,[segment[0],root.left.span[1]])
        snow_delivery(root.right,[root.right.span[0],segment[1]])
        
    root.sum = root.val + max(root.left.sum,root.right.sum)
    #print(root.span,root.sum,segment) 
         
    
def snow( T, I ):
    new_I=[]
    for i in range(len(I)):
            new_I.append(I[i][0])
            new_I.append(I[i][1])
    new_I.sort()
    uni = []
    uni.append(new_I[0])
    
    for i in range(1,len(new_I)):
        if new_I[i-1] != new_I[i]:
            uni.append(new_I[i])
            
    max_h = ceil(log2(len(uni)))
    tree = build_tree(max_h,T,uni)
    
    for i in I:
         snow_delivery(tree,i)
  
    return tree.sum

# n^2
def snow2( T, I):
    km = [0 for _ in range(T)]
    for p,k in I:
        for i in range(p,k+1):
            km[i]+=1
    return max(km)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

