def idec2ibin(n):
    print(f'({n})10 pra binário = ')
    inteira=''
    if n==1:
        print('1')
        return '1'
    elif n==0:
        print('0')
        return '0'
    while n>1:
        print(f'{n}/{2}')
        print(f'\tresultado {n//2}')
        print(f'\tresto {n%2}')
        inteira+=str(n%2)
        n=n//2
    inteira+=str(n)
    inteira=''.join(list(reversed(inteira)))
    return inteira

def dec2bin(n):
    n=float(n)
    inteira = int(n)
    decimal = n-inteira
    decbin = ''
    decimal*=2
    digito=int(decimal)
    decimal-=digito
    while decimal!=0:
        decbin += str(digito)
        decimal*=2
        digito=int(decimal)
        decimal-=digito
    decbin += str(digito)
    return bin(inteira)[2:],decbin

def ibin2idec(n):
    print(f'({n})2 para inteiro = ')
    n=str(n)
    n =''.join(list(reversed(n)))
    tam = len(n)
    s=0
    for i in range(tam):
        print(f'{n[i]}*2^{i} = {int(n[i])*2**(i)}')
        s+=int(n[i])*2**(i)
    return s

def bin2dec(n):
    inteira = n[:n.index('.')]
    decbin = n[n.index('.')+1:]
    decimal = 0
    cont = -1
    print(f'(0.{decbin})2 para real = ')
    for i in decbin:
        print(f'{i}*2^{cont} = {int(i)*2**cont}')
        decimal+=int(i)*2**cont
        cont-=1
    return ibin2idec(inteira),decimal
