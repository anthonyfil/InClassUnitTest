def Add(x, y):
    if(isinstance(x, int) and isinstance(y, int)):
        return x + y
    else:
        return "Error"
    
def Sub(x, y):
    if(isinstance(x, int) and isinstance(y, int)):
        return x - y
    else:
        return "Error"
    
def Mul(x, y):
    if(isinstance(x, int) and isinstance(y, int)):
        return x * y
    else:
        return "Error"
    
def Div(x, y):
    if(isinstance(x, int) and isinstance(y, int) and y != 0):
        return x / y
    else:
        return "Error"   
