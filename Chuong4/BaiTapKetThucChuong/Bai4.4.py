def nhap():
    print('Nhap 3 so nguyen:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a, b, c
def max3(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max
def inkq(kq):
    print('So lon nhat la:',kq)
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)


    