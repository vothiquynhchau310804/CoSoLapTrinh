def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        x=int(input())
        L.append(x)
    return L
def SoNguyenDuong(L):
    dem=0
    for i in L:
        if i>0:
            dem=dem+1
    print('SND=',dem,sep='')
def TrungBinhCongCacSoNguyenChan(L):
    tong=0
    demso=0
    for i in L:
        if i%2==0:
            tong=tong+i
            demso=demso+1
    if demso>0:
        TBC=tong/demso
        print('TBC=',TBC,sep='')
    elif demso==0:
        print('TBC=',0,sep='')
L=Input()
SoNguyenDuong(L)
TrungBinhCongCacSoNguyenChan(L)
    