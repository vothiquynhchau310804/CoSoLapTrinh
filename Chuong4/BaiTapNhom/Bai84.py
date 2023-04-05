def nhap():
    print('Nhap 3 so:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a, b, c
def trungvi(a,b,c):
    if a<b<c or c<b<c:
        return b
    elif b<c<a or a<c<b:
        return c
    elif b<a<c or c<a<b:
        return a
def inkq(kq):
    print('Trung vi cua 3 gia tri la:',kq)
a,b,c=nhap()
kq=trungvi(a,b,c)
inkq(kq)