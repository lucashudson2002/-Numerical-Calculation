import numpy as np

def substituicao(L, b, prints):
    n = len(b)
    x = np.ones((n,1))
    x[0]=b[0]/L[0,0]
    print(f'x{1} = {b[0]}/{L[0,0]}\n' if prints else '',end='')
    for i in range(1,n):
        s = b[i]
        print(f'x{i+1} = ({b[i]}' if prints else '',end='')
        for j in range(0,i):
            s = s - L[i,j]*x[j]
            print(f'+ {L[i,j]}*{x[j]}' if prints else '',end='')
        print(f')/{L[i,i]} =  {s/L[i,i]}\n' if prints else '',end='')
        x[i] = s/L[i,i]
    return x
    
def retro_substituicao(U, b, prints):
    n = len(b)
    x = np.ones((n,1))
    x[n-1]=b[n-1]/U[n-1,n-1]
    print(f'x{n} = {b[n-1]}/{U[n-1,n-1]} = {x[n-1]}\n' if prints else '',end='')
    for i in range(n-2,-1,-1):
        s = b[i]
        print(f'x{i+1} = ({b[i]}' if prints else '',end='')
        for j in range(i+1,n):
            s = s - U[i,j]*x[j]
            print(f'+ {U[i,j]}*{x[j]}' if prints else '',end='')
        print(f')/{U[i,i]} =  {s/U[i,i]}\n' if prints else '',end='')
        x[i] = s/U[i,i]
    return x   

def pivotamento(A, b, i):
    novaA=[]
    for j in range(len(A)):
        aux=[]
        for k in range(len(A)):
            aux.append(A[j,k])
        novaA.append(aux)
    A = novaA
    a=[abs(n[i]) if indice>=i else float('-inf') for indice, n in enumerate(A)]
    maxa  = max(a)
    indice = a.index(maxa)
    aux = A[indice]
    A[indice] = A[i]
    A[i]=aux
    aux = b[indice]
    b[indice] = b[i]
    b[i]=aux
    A = [np.array(n) for n in A]
    A = np.matrix(A)
    return A, b

def gaussiana(A,b,piv=False, prints=False):
    n=len(A)
    for k in range(n-1):
        print(f'{A}\n' if prints else '',end='')
        print(f'{b}\n' if prints else '',end='')
        if piv:
            A,b = pivotamento(A,b,k)
            print(f'{A}\n' if prints else '',end='')
            print(f'{b}\n' if prints else '',end='')
        for i in range(k+1,n):
            m=A[i,k]/A[k,k]
            print(f'm{i+1}{k+1} = {m}\n' if prints else '',end='')
            for j in range(k,n):
                A[i,j] = A[i,j] - m*A[k,j]
            b[i]=b[i]-m*b[k]
    print(f'{A}\n' if prints else '',end='')
    print(f'{b}\n' if prints else '',end='')
    x = retro_substituicao(A,b, prints)
    return x

def criterioLU(A):
    #det(Ak), k=1:n-1, diferente de 0
    n = len(A)-1
    for i in range(n):
        matriz = []
        for j in range(i+1):
            linha =[]
            for k in range(i+1):
                linha.append(A[j,k])
            matriz.append(linha)
        matriz = [np.array(j) for j in matriz]
        matriz=np.array(matriz)
        matriz=np.matrix(matriz)
        if round(np.linalg.det(matriz), 10)==0:
            return False
    return True

def decomposicaoLU(A):
    if not criterioLU(A):
        raise Exception('Matriz não pode ser decomposta em LU')
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    
    for i in range(0,n):
        for j in range(i,n):
            s=0
            k=0
            while k<=i:
                s+=L[i,k]*U[k,j]
                k+=1
            U[i,j]=A[i,j]-s
        L[i,i]=1
        for j in range(i+1,n):
            s=0
            k=0
            while k<=i:
                s+=L[j,k]*U[k,i]
                k+=1
            L[j,i]=(A[j,i]-s)/U[i,i]
    
    return L,U

def LU(A,b, prints=False):
    L,U=decomposicaoLU(A)
    print('L:\n' if prints else '',end='')
    print(f'{L}\n' if prints else '',end='')
    print('U:\n' if prints else '',end='')
    print(f'{U}\n' if prints else '',end='')
    print('Ly=b\n' if prints else '',end='')
    y = substituicao(L,b, prints)
    print('Ux=y\n' if prints else '',end='')
    x = retro_substituicao(U,y, prints)
    return x

def inversa(A, prints=False):
    n = len(A)
    L,U=decomposicaoLU(A)
    I = np.eye(n)
    y = []
    x = []
    for i in range(n):
        print(f'Ly = {I[i]}\n' if prints else '',end='')
        y.append(substituicao(L,I[i], prints))
    for i in range(n):
        print(f'Ux = {y[i]}\n' if prints else '',end='')
        x.append(retro_substituicao(U,y[i], prints))
        print(f'x{i+1}={x[i]}\n' if prints else '',end='')
    x = np.array(x)
    x = np.matrix(x)
    x = x.transpose()
    return x

def criterioG(A):
    #matriz ser simétrica, e det(Ak), k=1:n, maior que 0
    n = len(A)
    #pegandos os menores principais e vendo o det
    for i in range(n):
        matriz = []
        for j in range(i+1):
            linha =[]
            for k in range(i+1):
                linha.append(A[j,k])
            matriz.append(linha)
        matriz = [np.array(j) for j in matriz]
        matriz=np.array(matriz)
        matriz=np.matrix(matriz)
        if round(np.linalg.det(matriz), 10)<=0:
            return False
    #vendo se é simétrica
    for i in range(n):
        for j in range(i):
            if A[i,j]!=A[j,i]:
                return False
    return True

def decomposicaoG(A, prints):
    if not criterioG(A):
        raise Exception('Matriz não pode ser decomposta em GG^t')
    n = len(A)
    G = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            if j==i:
                s=0
                k=0
                print(f'G{i}{i} = raiz({A[i,i]} ', end='')
                while k<=(i-1):
                    s+=G[i,k]**2
                    print(f'- {G[i,k]}^2 ' if prints else '',end='')
                    k+=1
                G[i,i]=(A[i,i]-s)**(1/2)
                print(f') = raiz({A[i,i]-s}) = {G[i,i]}\n' if prints else '',end='')
            else:
                s=0
                k=0
                print(f'G{i}{j} = ({A[i,j]} ' if prints else '',end='')
                while k<=(j-1):
                    s+=G[i,k]*G[j,k]
                    k+=1
                    print(f'- {G[i,k]}*{G[j,k]} ' if prints else '',end='')
                G[i,j]=(A[i,j]-s)/G[j,j]
                print(f')/{G[j,j]} = {A[i,j]-s}/{G[j,j]} = {G[i,j]}\n' if prints else '',end='')
    return G

def cholesky(A,b, prints=False):
    G=decomposicaoG(A, prints)
    print('G:\n' if prints else '',end='')
    print(f'{G}\n' if prints else '',end='')
    print('GT:\n' if prints else '',end='')
    print(f'{G.transpose()}\n' if prints else '',end='')
    print('Gy=b\n' if prints else '',end='')
    y=substituicao(G,b, prints)
    print('GTx=y\n' if prints else '',end='')
    x=retro_substituicao(G.transpose(),y, prints)
    return x

def criterio_linhas(A):
    alfa = []
    n = len(A)
    for i in range(n):
        a=[]
        for j in range(n):
            if i!=j:
                a.append(A[i,j])
        alfa.append(abs(sum(a)/A[i,i]))
    maximo = max(alfa)
    if maximo<1:
        return True
    else:
        return False

def jacobi(A,b,x0,kmax, prints=False):
    if not criterio_linhas(A):
        raise Exception('Criterio de linhas para Jacobi não satisfeito')
    n = len(A)
    k=0
    x=x0[:]
    while k<kmax:
        print(f'\nk = {k}\n' if prints else '',end='')
        for i in range(n):
            print(f'x{i+1}={x[i]}\n' if prints else '',end='')
            j=0
            s1=0
            while j<=i-1:
                s1+=A[i,j]*x0[j]
                j+=1
            j=i+1
            s2=0
            while j<n:
                s2+=A[i,j]*x0[j]
                j+=1
            x[i] = (b[i]-s1-s2)/A[i,i]
        x0 = x[:]
        k+=1
    return x

def criterio_sanssefeld(A):
    beta = []
    n = len(A)
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                if len(beta)>=j:
                    s+=A[i,j]*beta[j]
                else:
                    s+=A[i,j]
        beta.append(abs(s/A[i,i]))
    maximo = max(beta)
    if maximo<1:
        return True
    else:
        return False
        
def gauss_seidel(A,b,x,kmax,prints=False):
    if not criterio_sanssefeld(A):
        raise Exception('Criterio de sanssefeld para Gauss-Seidel não satisfeito')
    n = len(A)
    k=0
    while k<kmax:
        print(f'\nk = {k}\n' if prints else '',end='')
        for i in range(n):
            print(f'x{i+1}={x[i]}\n' if prints else '',end='')
            j=0
            s1=0
            while j<=i-1:
                s1+=A[i,j]*x[j]
                j+=1
            j=i+1
            s2=0
            while j<n:
                s2+=A[i,j]*x[j]
                j+=1
            x[i] = (b[i]-s1-s2)/A[i,i]
        k+=1
    return x 

A=np.matrix('4 11.6035; 11.6035 33.7974', dtype=np.float64)
b=[9.1902, 27.1705]
x=cholesky(A,b,prints=True)
print(x)
#para ter o desenvolvimento da decomposiçaoLU olhar a U que é a gaussiana e os m que forma a L
