# def LaSoNguyenTo(x):
#     souoc=0
#     for i in range(1,x+1):
#         x%i==0
#         souoc+=1
#     if souoc==2:
#         return True
#     else:
#         return False
import math
def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        return True
def SoHopLe(x):
    if x <= 1:
        return True
    return False
def NhapVaDem():
    dem = 0
    print('Nhap day so:')
    while True:
        x = int(input())
        if SoHopLe(x):
            break
        elif LaSoNguyenTo(x):
            dem += 1
    return dem
def inKQ(kq):
    print('Co', kq, 'so nguyen to')
kq = NhapVaDem()
inKQ(kq)