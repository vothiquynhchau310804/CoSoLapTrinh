def Input():
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L
def count(L):
    dem=0
    for i in L:
        dem=dem+1
    print(dem)
L=Input()
count(L)
