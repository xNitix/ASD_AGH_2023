from zad2testy import runtests


class Node:
    def __init__ ( self ):
        self.edges = []
        self.weights = []
        self.ids = []
        self.waga = None

    def addEdge ( self, x, w, id ): 
            self.edges.append ( x )
            self.weights.append( w )
            self.ids.append( id )
            
def suma( T ):
    
    if len(T.edges) == 0:
        T.waga = 0
        return 0
    
    suma_ = 0
    
    for i in range(len(T.edges)):
        suma_ += suma(T.edges[i]) + T.weights[i]
        
    T.waga=suma_
    return suma_
        
def balance( T ):
    
    indx = 0
    
    def ktory( T , masa):
        inf = float("inf")
        nonlocal indx
        
        if len(T.edges) == 0:
            return masa
        
        min_loc = inf
        egde_indx = 0
        
        for i in range(len(T.edges)):
            if min_loc > abs((masa - (T.edges[i].waga + T.weights[i])) - T.edges[i].waga):
                min_loc = abs((masa - (T.edges[i].waga + T.weights[i])) - T.edges[i].waga)
                egde_indx = T.ids[i]
            
            ktory(T.edges[i], masa)

        
        if min_loc < ktory(T.edges[i], masa):
            indx = egde_indx
            return min_loc
        else:
            return ktory(T.edges[i], masa)
            

    masa = suma( T )
    ktory(T, masa)
    
    return indx
        
             
A = Node ()
B = Node ()
C = Node ()
D = Node ()
E = Node ()
A.addEdge (B, 6, 1 )
A.addEdge (C, 10, 2 )
B.addEdge (D, 5, 3 )
B.addEdge (E, 4, 4 )

print(balance(A))


    
runtests( balance )


