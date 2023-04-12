def nhap():
    a = float(input("Canh thu nhat: "))
    b = float(input("Canh thu hai: "))
    c = float(input("Canh thu ba: "))
    return a,b,c
def xuly(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def inkq(a,b,c):
    if xuly(a,b,c):
        print("Co the tao thanh mot tam giac.")
    else:
        print("Khong the tao thanh mot tam giac.")
a,b,c=nhap()
inkq(a,b,c)