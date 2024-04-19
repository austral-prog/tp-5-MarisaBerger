import math
def roots(a, b, c):
    discriminante = b**2 - 4*a*c 
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante))/2*a 
        r2 = (-b - math.sqrt(discriminante))/2*a 
        return f"({r1},{r2})"
    elif discriminante == 0:
        r1 = (-b + math.sqrt(discriminante))/2*a 
        return f"({r1})"
    else:
        return "()"
print(roots(1,2,3))

def value_y(a, b, c, x):
    y = (a*(x**2) + b*x +c)
    return y
print(value_y(1, -3, 2, 0))

def to_string(a, b, c):
    return f"f(x) = {a}*(x**2) + {b}*x + {c}"
print(to_string(2, -3, 1))
     
def derivation(a, b):
    return f"f´(x) = 2*{a}*x + {b}"
print(to_string(2, -3, 1))
