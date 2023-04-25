while True:
    a=input('a=')
    b=input('b=')
    if (a and b).isnumeric():
        print('a+b=',int(a)+int(b),sep='')
        break
    else:
        print('Khong hop le,nhap lai.')
        continue
