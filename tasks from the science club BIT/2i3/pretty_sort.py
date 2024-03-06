def make_new(num):
    count = [0 for _ in range(10)]
    num_copy = num
    while num_copy != 0:
        number = num_copy%10
        count[number]+=1
        num_copy = num_copy // 10
    sing_count = 0
    multi_count = 0
    for i in range(10):
        if count[i] == 1:
            sing_count+=1
        elif count[i] > 1:
            multi_count += 1
    return [(10-sing_count)*100 + multi_count,num]

def count_sort(T):
    n = len(T)
    C = [0 for _ in range(1011)]
    res = [0 for _ in range(n)]
    for i in range(n):
        C[T[i][0]] += 1
    for i in range(1,1011):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        res[C[T[i][0]]-1] = T[i][1]
        C[T[i][0]] -= 1
    for i in range(n):
        T[i] = res[i]


def pretty_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = make_new(T[i])
        
    count_sort(T)
    
    return T
