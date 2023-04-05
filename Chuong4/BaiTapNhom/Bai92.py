import math
def nhap():
    x=int(input('Nhap so nguyen: '))
    return x
def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
x=nhap()
if LaSoNguyenTo(x):
    print(x,'la so nguyen to')
else:
    print(x,'khong phai la so nguyen to')