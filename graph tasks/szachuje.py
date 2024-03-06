def make_graph(E,O):
    n = len(E)
    G = [[] for _ in range(n)]
    for v in O:
        G[v]=[False,E[v]]
    i = 0
    while i < n:
        if len(G[i]) == 0:
            G[i]=[True,E[i]]
        i+=1
    return G

def city_to_edges(G):
    n = len(G)
    edges=[]
    for i in range(n):
        for _ in G[i]:
            print(G[i][0])
            if not G[i][0]:
                for j in G[i][1]:
                    if G[j][0] == True:
                        if G[j][1][0] != i:
                            edges.append([True,[i,G[j][1][0]]])
                    else:
                        edges.append([False,[i,j]])
    return edges

def same_oaz(G,oasis):
    inf = float("inf")
    max = -inf
    for v in oasis:
        if v > max:
            max = v
    max+=1
    counter = 1
    matrix = [[None for _ in range(max)]for _ in range(max)]
    for E in G:
        if not E[0]:
            matrix[E[1][0]][E[1][1]] = counter
            matrix[E[1][1]][E[1][0]] = counter
            counter +=1
        elif E[0]:
            if matrix[E[1][0]][E[1][1]] == None:
                matrix[E[1][0]][E[1][1]] = True
                matrix[E[1][1]][E[1][0]] = True
    return matrix


                
oasis = [2, 4, 5, 7, 9]
graph = [[2, 4], [2, 9], [0, 4, 3], [2, 5], [0, 2, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1]]


G = make_graph(graph,oasis)
E = city_to_edges(G)
O = same_oaz(E,oasis)
print(O)

# 0 [[True, [2, 4]],
# 1 [True, [2, 9]],
# 2 [False, [0, 4, 3]],
# 3 [True, [2, 5]],
# 4 [False, [0, 2, 6]],
# 5 [False, [3, 7, 8]],
# 6 [True, [4, 7]],
# 7 [False, [5, 6, 8]],
# 8 [True, [5, 7]],
# 9 [False, [1]]]

# [[False, [2, 4]],
#  [False, [2, 4]],
#  [True, [4, 2]],
#  [False, [4, 2]],
#  [True, [4, 2]],
#  [False, [4, 2]],
#  [True, [5, 2]],
#  [False, [5, 7]],
#  [True, [5, 2]],
#  [False, [5, 7]],
#  [False, [7, 5]],
#  [True, [7, 4]],
#  [True, [7, 5]],
#  [False, [7, 5]],
#  [True, [7, 4]],
#  [True, [7, 5]],
#  [True, [9, 2]],
#  [True, [9, 2]]]

[[None, None, None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None, None, None],
 [None, None, None, None, 14, True, None, None, None, True],
 [None, None, None, None, None, None, None, None, None, None],
 [None, None, 14, None, None, None, None, True, None, None],
 [None, None, True, None, None, None, None, 18, None, None],
 [None, None, None, None, None, None, None, None, None, None],
 [None, None, None, None, True, 18, None, None, None, None],
 [None, None, None, None, None, None, None, None, None, None],
 [None, None, True, None, None, None, None, None, None, None]]