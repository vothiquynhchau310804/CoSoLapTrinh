#ham InSoNguyenTo(n) in lên màn hình các số là SNT trong dãy so từ 2 đến n
def Nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range(2,x):
        if x%2==0:
            return False
    return True
def InSoNguyenTo(n):
    for i in range(2,n+1):
        if LaSNT(i):
            print(i,end=' ')
            
n=Nhap()
InSoNguyenTo(n)