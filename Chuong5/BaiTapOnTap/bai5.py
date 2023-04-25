def Input():
    x=int(input())
    y=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x,y
def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y       
    print(L)
L,x,y=Input()
update(L,x,y)
     