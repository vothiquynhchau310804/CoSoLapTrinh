def Input():
    A=[]
    n=int(input('n='))
    for i in range(1,n+1):
        x=int(input())
        A.append(x)
    return A,n
def TongChan(A,n):
    tongchan=0
    for i in range(1,n,2):
        tongchan=tongchan+A[i]
    return tongchan
def InKQ(tongchan):
    print('Tong=',tongchan,sep='')
A,n=Input()
tongchan=TongChan(A,n)
InKQ(tongchan)