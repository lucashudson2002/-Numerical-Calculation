from decimal import Decimal as D
from math import log10, floor

def conta(x):
    x=str(x)
    return D(x)

def round_sig(x, n):
    return round(x, n-int(floor(log10(abs(x))))-1)

def lagrange(n, x, y, z):
    r=0
    for i in range(n):
        c=1
        d=1
        for j in range(n):
            if i!=j:
                c=c*(z-x[j])
                d=d*(x[i]-x[j])
        r = r+y[i]*(c/d)
    return r

import sympy as sp
def newton(x,y,z):
    n=len(x)
    dividida=[y]
    for i in range(1,n):
        ordem=[]
        for j in range(n-i):
            oanterior=dividida[i-1]
            elemento = round((conta(oanterior[j+1])-conta(oanterior[j]))/(conta(x[j+i])-conta(x[j])),4)
            ordem.append(elemento)
        dividida.append(ordem)
    for i in dividida:
        print(i)
    xx = sp.symbols('x')
    p=0
    for i in range(3):
        ordem=dividida[i][0]
        for j in range(i):
            ordem*=(xx-x[j])
        p+=ordem
    p=sp.expand(p)
    sp.pretty_print(p)
    p=sp.lambdify(xx,p)
    return p(z)
    
x=[1, 3, 5, 7, 9]
y=[1.01, 3.05, 5.13, 7.25, 9.42]
print(newton(x,y,5.3))
