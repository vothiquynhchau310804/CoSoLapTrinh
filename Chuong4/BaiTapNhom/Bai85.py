def nhap():
    n=int(input('Nhap tu 1 den 12: '))
    return n
def xuly(n):
    if n==1:
        return 'first'
    elif n==2:
        return 'second'
    elif n==3:
        return 'third'
    elif n==4:
        return 'fourth'
    elif n==5:
        return 'fifth'
    elif n==6:
        i='sixth'
        return 'sixth'
    elif n==7:
        return'seventh'
    elif n==8:
        return'eighth'
    elif n==9:
        return'ninth'
    elif n==10:
        return 'tenth'
    elif n==11:
        return 'eleventh'
    elif n==12:
        return 'twelfth'
    else:
        return''
def inkq(kq):
    print(kq)   
n=nhap()
kq=xuly(n)
inkq(kq)     
