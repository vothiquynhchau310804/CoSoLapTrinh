import math
print('Nhap ba canh cua tam giac:')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if (a+b>c) and (a+c>b) and (b+c>a):
    p=(a+b+c)/2
    dientich=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Dien tich=',round(dientich,3))
else:
    print('Khong hop le')