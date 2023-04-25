def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        x=int(input())
        L.append(x)
    x=int(input('x='))
    return L,x
def FirstAndLast(L):
    pt=[L[0],L[-1]]
    return pt
def Search(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return True
    return False
L,x=Input()
FirstAndLast(L)
print(FirstAndLast(L))
Search(L,x)
print(Search(L,x))