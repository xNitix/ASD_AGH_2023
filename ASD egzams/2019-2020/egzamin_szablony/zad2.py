from zad2testy import runtests

def opt_sum(tab):
    n = len(tab)
    inf = float("inf")
    matrix = [[inf for _ in range(n)]for _ in range(n)]
    def sum_rek(matrix,tab,i,j):
        inf = float("inf")
        if matrix[i][j] != inf:
            return matrix[i][j]
        if j == i+1:
            matrix[i][j] = abs(tab[i] + tab[j])
            return matrix[i][j]
        return max(abs(sum(tab[i:j+1])),min(sum_rek(matrix,tab,i+1,j),sum_rek(matrix,tab,i,j-1)))
    return sum_rek(matrix,tab,0,len(tab)-1)



runtests( opt_sum )
