def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    while n>=0:
        gt=1
        if n==0:
            return gt
        else:
            for i in range(1,n+1):
                gt=gt*i
            return gt
def inkq(n,X):
    print('{0}!={1}'.format(n,X))
n=nhap()
X=giaithua(n)
inkq(n,X)