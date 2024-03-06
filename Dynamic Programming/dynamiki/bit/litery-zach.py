from collections import deque
def word(s):
    n = len(s)
    cnt = [0]*26
    v = [False]*26
    Que = deque()
    
    for c in s:
        cnt[ord(c) - 97] += 1
        
    Que.append(s[0])
    cnt[ord(s[0]) - 97] -= 1
    v[ord(s[0]) - 97] = True
    
    for i in range(1,n):
        c = s[i]
        
        if v[ord(c) - 97]:
            cnt[ord(c) - 97] -= 1
            continue
        
        while Que:
            stack_c = Que.pop()
            if c < stack_c and cnt[ord(stack_c) - 97] > 0:
                v[ord(stack_c) - 97] = False
                Que.append(c)
                v[ord(c) - 97] = True
                cnt[ord(c) - 97] -= 1
                break
                
            else:
                Que.append(stack_c)
                Que.append(c)
                v[ord(c) - 97] = True
                cnt[ord(c) - 97] -= 1
                break
    
    res = ""
    while Que:
        c = Que.popleft()
        res += c
    
    return res


string = "cbacdcbc"

print(word(string))            
                
            
    