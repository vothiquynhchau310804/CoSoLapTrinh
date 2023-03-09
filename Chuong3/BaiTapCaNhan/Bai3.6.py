print('Nhap ba canh cua tam giac:')
a=float(input())
b=float(input())
c=float(input())
if (a+b>c) and (a+c>b) and (b+c>a):
    if (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==b*b+a*a):
        print('Tam giac vuong')
    elif (a == b) or (b == c) or (c == a):
        print('Tam giac deu')
    else:
        print('Tam giac loai khac')
else:
    print('Khong hop le')