import math
from math import sqrt


def ptb1(a,b):
    if a == 0 and b == 0:
        return 'Infinity'
    elif a == 0 and b != 0:
        return "No solution"
    else:
        return -b/a
def ptb2(a,b,c):
    if a==0:
        return ptb1(a,b)
    elif a==0 and b==0 and c==0:
        return 'Infinity'
    elif a==0 and b==0:
        return 'No Solution'
    else:
        delta=(b**2)-4*a*c
        if delta<0:
            return 'No Solution'
        elif delta==0:
            x=(-b/(2*a))
            return 'x1=x2='+str(x)
        else:
            x1= (-b+math.sqrt(delta))/(2*a)
            x2= (-b-math.sqrt(delta))/(2*a)
            return 'x1='+str(x1)+" "+'x2='+str(x2)