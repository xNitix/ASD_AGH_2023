def cut(rect1, rect2):
    x11, y11, x12, y12 = rect1
    x21, y21, x22, y22 = rect2
    x1 = max(x11, x21)
    y1 = max(y11, y21)
    x2 = min(x12, x22)
    y2 = min(y12, y22)
    return x1, y1, x2, y2


def rect_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

def rect(T):
    n = len(T)
    
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    mid = [0 for _ in range(n)]
    left[0] = T[0]
    right[n-1] = T[n-1]
    
    for i in range(1,n):
        left[i] = cut(T[i-1],T[i])
    
    for i in range(n-2,-1,-1):
        right[i] = cut(T[i+1],T[i])
        
    mid[0] = rect_area(right[1][0],right[1][1],right[1][2],right[1][3])
    mid[n-1] = rect_area(left[n-2][0],left[n-2][1],left[n-2][2],left[n-2][3])
    
    for i in range(1,n-1):
        mid[i] = rect_area(*cut(left[i-1],right[i+1]))
        
    return mid.index(max(mid))

D = [(2,3,10,6),(3,1,8,8),(5,4,9,7)]

print(rect(D))
    
    