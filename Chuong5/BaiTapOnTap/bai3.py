def Input():
    x=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x
def delete(L,x):
    i=0
    while i<len(L):
        if x==L[i]:
            L=L[:i]+L[i+1:]
        else:
            i=i+1
    print(L)
L,x=Input()
delete(L,x)
