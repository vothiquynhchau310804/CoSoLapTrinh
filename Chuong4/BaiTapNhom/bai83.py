def mathang():
    print('So mat hang la:')
    n=int(input('n='))
    return n
def tinhtien(n):
    if n==1:
        s=10.95
    for i in range(2,n+1):
        s=10.95+2.95*(i-1)
    return s
def inkq(s):
    print('Phí vận chuyển là:',round(s,2))
n=mathang()
s=tinhtien(n)
inkq(s)