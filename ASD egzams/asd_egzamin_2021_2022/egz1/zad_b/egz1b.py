# Numeruje po koleji wierzcholkii (global vertex_number), oraz kazdemu przypisuje na jakim jest poziomie (symber,wys). Zamieniam drzewo na graf i tworze tablice ktorej zadanie jest, pod
# i-tym indeksem trzymac ile wierzcholkow znajduje sie na itej wysokosci (ich ilosc to szerokosc drzewa). Znajduje max wysokosc i szerokosc i ustaiwam wszystkie wierzcholki na tej wysokosci
# na true w tablicy vertex_in_tree. Potem przelatuje po tej tablicy od tylu tak by pominac wierzcholki powyzej wysokosci i jesli wierzcholek na true to jego parenta tez daje na true. W taki
# sposob mam liste wierzcholkow ktore sa z szukanym drzewie i pod koniec licze ile krawedzi musze usunac, czyli ile krawdzi z wierzcholkow z true wychodzi do wierzcholkow z false.

from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.wys = None       # pole do wykorzystania przez studentow
    self.number = None
    
    
vertex_number=0
maxi = 0
def numeracja(root,i=0):
  global vertex_number
  root.wys = i
  root.number = vertex_number
  vertex_number += 1
  if root.left != None:
    numeracja(root.left,i+1)
  if root.right != None:
    numeracja(root.right,i+1)
  global maxi 
  maxi = max(maxi,i)
  
def make_graph(root):
  global vertex_number
  global maxi 
  graph = [[]for _ in range(vertex_number)]
  H = [0 for _ in range(maxi+1)]
  
  def make(root,graph,H):
    #left
    if root.left != None:
      graph[root.number].append(root.left.number)
      graph[root.left.number].append(root.number)
      make(root.left,graph,H)
    
    #right
    if root.right != None:
      graph[root.number].append(root.right.number)
      graph[root.right.number].append(root.number)
      make(root.right,graph,H)
    
    H[root.wys] += 1
    
  make(root,graph,H)
  
  return graph,H

def wideentall( T ):
    numeracja(T)
    graph,H = make_graph(T)
    global vertex_number
    global maxi
    
    max_H = 0
    max_W = 0
    
    for i in range(len(H)-1,-1,-1):
      if H[i] > max_W:
        max_H = i
        max_W = H[i]
        
    vertex_in_tree = [False for _ in range(vertex_number)]
    
    def in_tree(root,h,tab):
      if root.wys == h:
        tab[root.number] = True
      if root.left != None:
        in_tree(root.left,h,tab)
      if root.right != None:
        in_tree(root.right,h,tab)
        
    in_tree(T,max_H,vertex_in_tree)
    
    for i in range(len(vertex_in_tree)-1,-1,-1):
      if vertex_in_tree[i]:
        for j in graph[i]:
          if j < i:
            vertex_in_tree[j] = True
            
    def to_cut_counter(root,tab):
      res = 0
      if root.left != None:
        if tab[root.left.number]:
          res += to_cut_counter(root.left,tab)
        else:
          res+=1
      if root.right != None:
        if tab[root.right.number]:
          res += to_cut_counter(root.right,tab)
        else:
          res+=1
      return res

    vertex_number = 0
    maxi = 0

    return to_cut_counter(T,vertex_in_tree)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )
