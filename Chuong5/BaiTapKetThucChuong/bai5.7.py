def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        x=int(input())
        L.append(x)
    return L
def LoaiBo(L):
    M=[]
    for i in L:
        if i not in M:
            M.append(i)
    # print(M)
    for i in M:
        print(i,end=' ')
L=Input()
LoaiBo(L)