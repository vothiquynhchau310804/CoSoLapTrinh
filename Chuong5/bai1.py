def Input():
    x=int(input())
    k=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x,k
def add(L,x,k):
    if k>len(L):
        L=L+[x]
    elif k==0:
        L=[x]+L
    else:
        L=L[:k]+[x]+L[k:]
    print(L)
L,x,k=Input()
add(L,x,k)


