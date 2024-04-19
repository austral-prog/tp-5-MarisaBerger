import math
def roots(a, b, c):
    discriminante = b**2 - 4*a*c 
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante))/2*a 
        r2 = (-b - math.sqrt(discriminante))/2*a 
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r1 = (-b + math.sqrt(discriminante))/2*a 
        return f"({r1})"
    else:
        return "( )"

def value_y(a, b, c, x):
    y = (a*(x**2) + b*x +c)
    return y

def to_string(a, b, c):
    if (a == 0 and b == 0):
        return f"f(x) = {c}"
    elif a == 0 :
        return f"f(x) = {b} * X + {c}"
    elif (b == 0):
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
     
def derivation(a, b, c):
    if (a == 0 and b ==0):
        return f"f'(x) = {b}"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"
