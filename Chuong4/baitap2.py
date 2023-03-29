# Hàm Nhap() nhập từ bàn phím một số nguyên n
# hàm LaSNT(x) trả về True nếu x là SNT, còn lại trả về False
#hàm InKQ(n) sử dụng hàm LaSNT(x) để kiểm tra n có ohair là SNT hay không, in lên màn hình kết qua theo mẫu sau
def Nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def InKQ(n):
    if LaSNT(n):
        print(n,'la SNT')
    else:
        print(n,'khong la SNT')
n=Nhap()
InKQ(n)