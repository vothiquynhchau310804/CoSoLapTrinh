def Input():
    x=int(input())
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L,x
def search(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return i
    return None        
L,x=Input()
search(L,x)
print(search(L,x))