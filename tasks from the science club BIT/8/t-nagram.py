def is_tenegram(x,y,t):
    if len(x) != len(y):
        return False
    
    n = len(x)
    letters = [0 for _ in range(27)]
    
    for i in range(n):
        letters[ord(x[i])-97] += 1
    
    for i in range(n):
        letters[ord(y[i])-97] -= 1
        
    for i in range(n):
        if letters[i] != 0:
            return False
    
    letters = [0 for _ in range(27)]
    
    for i in range(t+1):
        letters[ord(x[i])-97] += 1
    
    j = 0
    for i in range(n-t):
        
        if i != 0:
            letters[ord(x[t + i])-97] += 1
            if j > t:
                letters[ord(x[j-t-1])-97] -= 1
                
        if letters[ord(y[j])-97] <= 0:
            return False
        else:
            j+=1
            
    while j < n:
        letters[ord(x[j-t-1])-97] -= 1
        
        if letters[ord(y[j])-97] <= 0:
            return False
        else:
            j+=1
    
    return True

x = "kotomysz"
y = "tokmysoz"
t = 2
print(is_tenegram(x,y,t))
            
    
        
    
    