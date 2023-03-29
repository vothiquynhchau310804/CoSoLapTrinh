import math
def nhap():
    print('Cac canh của tam giac la:')
    a=int(input('a='))
    b=int(input('b='))
    return a,b
def xuly(a,b):
    if a>0 and b>0:
        n=math.sqrt(a**2+b**2)
        return n
def inkq(n):
    print('Canh huyen =',n)
a,b=nhap()
n=xuly(a,b)
inkq(n)