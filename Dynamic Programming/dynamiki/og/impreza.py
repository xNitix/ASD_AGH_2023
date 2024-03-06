class Employee:
    def __init__(self, fun, employees=[]):
        self.fun = fun
        self.f = -1
        self.g = - 1
        self.emp = employees
        
    def __str__(self):
        return f"Fun: {self.fun:<5} f: {self.f:<5} g: {self.g:<5}"
        
    
def f(v):
    if v.f < 0:
        x = v.fun
        for e in v.emp:
            x += g(e)
        y = g(v)
        v.f = max(x, y)
    return v.f
    
    
def g(v):
    if v.g < 0:
        v.g = 0
        for e in v.emp:
            v.g += f(e)
    return v.g