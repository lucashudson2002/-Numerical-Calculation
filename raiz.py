import numpy as np

def bissecao(f,a,b,emax,kmax=float('inf')):
    k=0
    erro = float('inf')
    x=None
    while k<kmax and abs(erro)>emax:
        print(f'\nk = {k}')
        print(f'a = {a}')
        print(f'b = {b}')
        x = (a+b)/2
        x = float(f'{x:.8}')
        print(f'xk = {x}')
        print(f'f(a) = {f(a)}')
        print(f'f(b) = {f(b)}')
        print(f'f(xk) = {f(x)}')
        if f(a)*f(x)<0:
            b = x
        else:
            a = x
        erro = f(x)
        k+=1
    return x,k

def falsa_posicao(f,a,b,emax,kmax=float('inf')):
    k=0
    erro = float('inf')
    x=None
    while k<kmax and abs(erro)>emax:
        print(f'\nk = {k}')
        print(f'a = {a}')
        print(f'b = {b}')
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        x = float(f'{x:.8}')
        print(f'xk = {x}')
        print(f'f(a) = {f(a)}')
        print(f'f(b) = {f(b)}')
        print(f'f(xk) = {f(x)}')
        if f(a)*f(x)<0:
            b = x
        else:
            a = x
        erro = f(x)
        k+=1
    return x,k

#fi e fi' continuas, sendo |fi'|<1
def ponto_fixo(fi, f, x, emax,kmax=float('inf')):
    k=0
    erro = float('inf')
    while k<kmax and abs(erro)>emax:
        print(f'\nk = {k}')
        print(f'xk = {x}')
        print(f'f(xk) = {f(x)}')
        x = fi(x)
        x = float(f'{x:.8}')
        erro = f(x)
        k+=1
    return x

def newton(f,df,x,emax,kmax=float('inf')):
    k=1
    erro = float('inf')
    while k<kmax and abs(erro)>=emax:
        print(f'\nk = {k-1}')
        print(f'xk = {x}')
        print(f'f\'(xk) = {df(x)}')
        print(f'f(xk) = {f(x)}')
        x = x - (f(x)/df(x))
        x = float(f'{x:.5}')
        erro = abs(f(x))
        k+=1
    print(f'\nk = {k-1}')
    print(f'xk = {x}')
    print(f'f\'(xk) = {df(x)}')
    print(f'f(xk) = {f(x)}')
    return x,k-1

def secante(f,x0,x1,emax,kmax=float('inf')):
    k=2
    x=None
    erro = float('inf')
    print(f'x{0} = {x0}')
    print(f'fx{0} = {f(x0)}')
    print(f'x{1} = {x1}')
    print(f'fx{1} = {f(x1)}')
    while k<kmax and abs(erro)>emax:
        d= (f(x1)-f(x0))/(x1-x0)
        x = x1 - f(x1)/d
        x = float(f'{x:.8}')
        x0=x1
        x1=x
        print(f'\nx{k} = {x1}')
        print(f'fx{k} = {f(x1)}')
        erro = f(x)
        k+=1
    return x,k-2

def f(x):
    return np.log(x)-1

def df(x):
    return 1/x

def fi(x):
    return 

print(newton(f,df,1,1e-4))
#o erro tá em todos sendo f(x), dependendo via precisar mudar
