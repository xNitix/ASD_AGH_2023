from queue import Queue

class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None
    
        
def ValuableTree(T,k):
    vertex_num = 0
    
    def get_vertex_number(V):
        nonlocal vertex_num
        V.X = vertex_num
        vertex_num += 1
        if V.left != None:
            get_vertex_number(V.left)
        if V.right != None:
            get_vertex_number(V.right)

    get_vertex_number(T)
    
    dp = [[0 for _ in range(vertex_num+1)]for _ in range(k+1)]
    
    T_copy = T
    Que = Queue()
    Que.put(T_copy)
    while not Que.empty():
        T_curr = Que.get()
        dp[1][T_curr.X] = max(T_curr.leftval,T_curr.rightval)
        if T_curr.left != None:
            Que.put(T_curr.left)
        if T_curr.right != None:
            Que.put(T_curr.right)
    
    def f(V,k_c):
        if V == None:
            return 0
        if dp[k_c][V.X] != 0:
            return dp[k_c][V.X]
        elif k_c > 0 :
            v = max(f(V.left,k_c-1)+V.leftval,f(V.right,k_c-1)+V.rightval)
            for j in range(1,k_c):
                v = max(v,f(V.left,j-1)+V.leftval + f(V.right,k_c-j-1)+V.rightval)
            dp[k_c][V.X] = v
            return v
        else:
            return 0
        
    T_copy2 = T
    Que = Queue()
    Que.put(T_copy2)
    while not Que.empty(): 
        t_curr = Que.get()
        for i in range(2,k+1):
            f(t_curr,i)
        if t_curr.left != None:
            Que.put(t_curr.left)
        if t_curr.right != None:
            Que.put(t_curr.right)
    
    return max(dp[k])
    
F = Node()
G = Node()
D = Node()
E = Node()
C = Node()
C.left = F
C.leftval = 8
C.right = G
C.rightval = 10
B = Node()
B.left = D
B.leftval = 6
B.right = C
B.rightval = 2
A = Node()
A.left = B
A.leftval = 1
A.right = E
A.rightval = 5
k = 3

print(ValuableTree(A,k))
