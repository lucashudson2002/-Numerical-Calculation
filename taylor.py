import numpy as np
import math

def parcela(x,i):
    return (x**i)/math.factorial(i) #Pn para e^x em torno de a=0

def taylor(x, n):
    resposta=0
    for i in range(n+1):
        resposta+=parcela(x,i)
    return resposta

print(taylor(2,20))
