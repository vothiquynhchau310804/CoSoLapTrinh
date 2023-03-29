import math
def nhap():
    print('Nhap 3 so nguyen:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a, b, c
def giaipt(a, b, c):
    global x1, x2
    global delta
    delta = b**2-4*a*c
    if delta == 0:
        x1 = x2 = -b/(2*a)
    elif delta > 0:
        x2 = float((-b - math.sqrt(delta)) / (2 * a))
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
def inkq():
    if delta > 0:
        print('Phuong trinh co hai nghiem')
        print('x1=', x1,sep='')
        print('x2=', x2,sep='')
    elif delta == 0:
        print('Phuong trinh co nghiem kep')
        print('x1=x2=', x1, sep='')
    else:
        print('Phuong trinh vo nghiem')
a, b, c = nhap()
giaipt(a, b, c)
inkq()