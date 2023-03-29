# viết chương trình thực hiện các yêu cầu sau
# - hàm nhap(): Nhập từ bàn phím một số nguyên n và trả về qua tên hàm
# - hàm LaSoDuong(x): hàm kiểm tra số nguyên x, nếu x<=0 thì trả về 0, còn lại trả về 1
# -Hàm Xuly(): nhập từ bàn phím n số nguyên, trả về số lượng số nguyên dương và chẵn, yêu cầu sử dụng hàm LaSoDuonf(x)để kiểm đếm
# -hàm InKQ(soluong): in lên màn hình giá trị biến soluong, theo mau:
#     Co<soluong>so nguyen duong va chan
# vd n=5
#     2
#     -4
#     5
#     6
#     -7
#     Có 2 so nguyen duong va chan
def Nhap():
    n=int(input('n='))
    return n
def LaSoDuong(x):
    if x>0 and x%2==0:
        return 1
    else:
        return 0
def XuLy(n):
    dem=0
    for i in range(1,n+1):
        x=int(input())
        if LaSoDuong(x)==1:
            dem=dem+1
    return dem
def InKQ(soluong):
    print('Co',soluong,'so nguyen duong va chan')
n=Nhap()
soluong=XuLy(n)
InKQ(soluong)
